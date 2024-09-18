what I need to do:

- a python script which I can use to add contex as files for Claude API to use (attach source code)
    - already did POC. simply attach file as text into the prompt with markdown syntax highlighting + dirs support!
- set a system prompt
    - keep a system prompt with knowledge base in XML for the LLM to use
        - basic POC done. yet to extract XML knowledge base and build it for system prompt. currently it's all one file. todo
- probably it should be a prompt I type in a file and then fire off `python -i llm.py' and get a response as a new file in my repository of files for this project
    - still thinking about the ideal way to chat. probably just get used to alt/option + Enter key combo to make conversation for now. do not prematurely automate. abstraction is not your friend. it is an enemy you must join forces with in order to defeat a bigger evil: complexity
- maintain a tight devloop along the use of frontier models, use Claude Sonnet 3.5 to the max
    - yet to think about how a tight dev loop can be acheieve. so far only on a python notebook. code editor extension? todo study existing tools like mentat, supermaven, avante.nvim
