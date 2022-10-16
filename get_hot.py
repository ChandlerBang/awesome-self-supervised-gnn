"""Mark hot articles which are extensively cited"""

import re
from tqdm import tqdm
import time
import os
import subprocess
import scholar
import numpy as np


def overlap(s1, s2):
    s1 = replace(s1)
    s2 = replace(s2)
    s1 = set(s1.split())
    s2 = set(s2.split())
    intersec = s1 & s2
    return len(intersec)/len(s1)

def replace(s0):
    s0 = s0.replace('.', ' ')
    s0 = s0.replace(':', ' ')
    s0 = s0.lower()
    return s0

def get_citations(paper, verbose=1):
    def searchScholar(searchphrase, title):
        query = scholar.SearchScholarQuery()
        # query.set_words(searchphrase)
        query.set_words(title)
        querier.send_query(query)
        articles = querier.articles
        try:
            if overlap(articles[0].attrs['title'][0], title) < 0.9:
                return 0
        except:
            # set_new_proxy()
            return -1
        return articles[0].attrs['num_citations'][0]

    art = ["-c", "1", "--phrase", paper]
    querier = scholar.ScholarQuerier()
    settings = scholar.ScholarSettings()
    settings.set_citation_format(2)
    querier.apply_settings(settings)
    cites = searchScholar(art, paper)
    while cites == -1:
        searchScholar(art, paper)
    if verbose:
        print(f'{paper}: ', cites)
    return cites

def get_papers(filename):
    papers = []
    paper2line = {}
    with open(filename, 'r') as f:
        for num, line in enumerate(f.readlines()):
            if 'Other related papers' in line: # do not count them
                break
            if '[paper]' in line:
                res = re.findall('\*\*.+\*\*', line)[0]
                res = res[2:-2]
                paper2line[len(papers)] = num
                papers.append(res)
                print(res)
    return papers, paper2line

papers, paper2line = get_papers('README.md')
citations = []
for id, p in tqdm(enumerate(papers)):
    time.sleep(2)
    citations.append(get_citations(p))

idx = np.arange(len(citations))
citations = np.array(citations)
hot_id = idx[citations>80]

with open('README.md', 'r') as f:
    content = f.readlines()

with open('README_old.md', 'w') as f:
    f.write(' '.join(content))

for p in hot_id:
    line = paper2line[p]
    old_content = content[line]
    num = re.findall(r'\d+', old_content)[0] # the number before '.'
    new_content = old_content[:len(num)+2] + ":fire:" + old_content[len(num)+2:]
    content[line] = new_content
with open('README.md', 'w') as f:
    f.write(' '.join(content))
