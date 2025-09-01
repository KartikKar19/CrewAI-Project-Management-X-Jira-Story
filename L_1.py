#!/usr/bin/env python
# coding: utf-8

# # L1: Automated Project: Planning, Estimation, and Allocation

# <p style="background-color:#fff6e4; padding:15px; border-width:3px; border-color:#f5ecda; border-style:solid; border-radius:6px"> ⏳ <b>Note <code>(Kernel Starting)</code>:</b> This notebook takes about 30 seconds to be ready to use. You may start and watch the video while you wait.</p>

# ## Initial Imports
from helper import get_openai_api_key
print("Loaded API key (first 8 chars):", get_openai_api_key()[:8])

# In[ ]:


# Warning control
import warnings
warnings.filterwarnings('ignore')

# Load environment variables
from helper import load_env
load_env()

import os
import yaml
from crewai import Agent, Task, Crew


# <p style="background-color:#fff6ff; padding:15px; border-width:3px; border-color:#efe6ef; border-style:solid; border-radius:6px"> 💻 &nbsp; <b>Access <code>requirements.txt</code> and <code>helper.py</code> files:</b> 1) click on the <em>"File"</em> option on the top menu of the notebook and then 2) click on <em>"Open"</em>. For more help, please see the <em>"Appendix - Tips and Help"</em> Lesson.</p>

# ## Set OpenAI Model

# In[ ]:


os.environ['OPENAI_MODEL_NAME'] = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")


# ## Loading Tasks and Agents YAML files

# In[ ]:


# Define file paths for YAML configurations
files = {

  # This file has been modularized. Please use main.py to run the project pipeline.
}


