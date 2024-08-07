from langchain_community.llms import Ollama
from Dataloader import loader as ld

def model(filePath,project_description,user_guidlines):
    print("model is called")
    # Model
    model = Ollama(model='CodeChecker')

    # Extracting code from a file
    code = ld(filePath)
    print(code)

    # Projext Describtion
    project_description=project_description

    # User Guidlines
    user_guidlines=user_guidlines

    # Prompt
    prompt = """
        Review and check whether the the submitted code according to the client's project description.For correcteness you will Run unit test by yourself with real examples.User may also provide specific code guidelines and principles so you have to check whether the provided code meet the principles and guidelines. 
        Respond as yes or no if the program is correct or incorrect,respectively,and if it is wrong then only then give all the fixes once.
        Keep it simple,short and concise.
    """

    # Complete Template COntaing all informations
    template = f"""
    prompt:
    {prompt}

    User Provided Guidlines and Principles:
    {user_guidlines}

    Project Description:
    {project_description}

    Submitted Code:
    {code}
        """
    # Passing Template and waiting for response
    print("Generating response")
    response = model.invoke(template)

    print(response)

    return response

# model('./files/app.py','python Program to find the area of triangle','')