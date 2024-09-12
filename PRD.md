what I need to do:

- a python script which I can use to add contex as files for Claude API to use (attach source code)
    - already did POC. simply attach file as text into the prompt with markdown syntax highlighting
        - mark the file names for multiple files
        - when it comes time to automate this, give it a dir or list of files and have it add all files automatically
            - cache this prompt! this is huge for library use.
                - use this for work as well. try to run a crawler on DSP documentation and feed it to the LLM. this is an old dream of mine. I can automate away so much work and rise up and overcome
- set a system prompt
    - keep a system prompt with knowledge base in XML for the LLM to use
        - basic POC done. yet to extract XML knowledge base and build it for system prompt. currently it's all one file. todo
- probably it should be a prompt I type in a file and then fire off `python llm.py' and get a response as a new file in my repository of files for this project
    - still thinking about the ideal way to chat. probably just get used to alt/option + Enter key combo to make conversation for now. do not prematurely automate. abstraction is not your friend. it is an enemy you must join forces with in order to defeat a bigger evil: complexity
- maintain a tight devloop along the use of frontier models, use Claude Sonnet 3.5 to the max
    - yet to think about how a tight dev loop can be acheieve. so far only on a python notebook