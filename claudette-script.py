#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('ANTHROPIC_API_KEY') as f: DO_NOT_FUCKING_COMMIT_TO_GIT = f.read()


# In[2]:


import os
os.environ['ANTHROPIC_API_KEY'] = DO_NOT_FUCKING_COMMIT_TO_GIT
# os.environ['ANTHROPIC_LOG'] = 'debug'


# In[3]:


from claudette import *
sonnet35 = models[1]
opus3 = models[0]


# In[4]:


def get_syntax_id(filename):
    extension = os.path.splitext(filename)[1].lower()
    syntax_map = {
        '.py': 'python',
        '.html': 'html',
        '.js': 'javascript',
        '.css': 'css',
        '.md': 'markdown',
        # add more mappings as needed
    }
    return syntax_map.get(extension, '')

def f_md_str(filepath:str, custom_filename:str=None) -> str:
    """reads file as a markdown code snippet"""
    # print(f"f_md_str invoked with {filepath=}, {syntax_id=}, {custom_filename=}")
    with open(filepath, 'r') as f: content = f.read()
    filename = custom_filename or os.path.basename(filepath)
    syntax_id = get_syntax_id(filename)
    file_content = f"### {filename}\n\n```{syntax_id}\n{content}\n```\n"
    return file_content

def dir_md_str(directory:str) -> []:
    """reads directory as markdown code snippets. adds relative paths as headers for dir structure hints"""
    result = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if not os.path.basename(filename).startswith('.'):  # skip hidden files
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, directory)
                result.append(f_md_str(filepath, rel_path))
    return result

def update_file(
    filepath:str, # The path of the file to update. if not provided
    content:str # The content to replace the contents with
) -> bool:
    """write content to file. tool for Claude to update files on my system"""
    with open(filepath, 'w') as o: o.write(content)
    return True


# In[5]:


with open('prompts/system-prompt.md') as f: sp = f.read()
chat = Chat(sonnet35, sp=sp, tools=[update_file])


# In[ ]:


chat("hi Claude what's good")

