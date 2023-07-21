from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


from dotenv import load_dotenv


load_dotenv()


llm = OpenAI(temperature=0.1)

# Here prompt creation and generation 
    
def generate_diagnostic_steps():

    prompt_template_name = PromptTemplate(
        input_variables=['customer_issue'],
        #template = " Please give me the diagnostic setps for this {customer_issue}. suggest me step by step procedure")
        template = " give me the diagnostic steps for  {customer_issue}. suggest me fancy name")

    diag_chain =  LLMChain(llm =llm, prompt=prompt_template_name)

    diag_chain.run("vxlan")
    
        
    response = diag_chain.run("evpn")
    




def main():
      
    response = generate_diagnostic_steps()
    print(response)



if __name__ =="__main__":
    main()