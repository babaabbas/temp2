import os
import textwrap
import sys
print(sys.path)
import langchain
sys.path.append('<path_to_langchain_installation>')
from langchain_community.document_loaders.text import TextLoader
from scraper import extract_text_from_pdf,get_text_from_url
from data import extract_info_from_mongodb



url = 'https://www.forbesindia.com/blog/'
url2='https://www.forbesindia.com/innovation/1887/1'
url3='https://www.forbesindia.com/life/92/1'
path1 = "/Users/abbasbaba/PycharmProjects/hackathon/pd1.pdf"
path2="/Users/abbasbaba/PycharmProjects/hackathon/pdf2.pdf"
path3="/Users/abbasbaba/PycharmProjects/hackathon/pdf3.pdf"
path4="/Users/abbasbaba/PycharmProjects/hackathon/pdf4.pdf"

text = get_text_from_url(url)+get_text_from_url(url2)+get_text_from_url(url3)+extract_text_from_pdf(path1)+extract_text_from_pdf(path2)+extract_text_from_pdf(path3)+extract_text_from_pdf(path4)
file_path = "abs.txt"
with open(file_path, 'w') as file:
    file.write(text)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
loader = TextLoader('/Users/abbasbaba/PycharmProjects/hackathon/abs.txt')
loader2=TextLoader('/Users/abbasbaba/PycharmProjects/hackathon/users.txt')
documents = loader.load()
try:
    from langchain.embeddings import HuggingFaceEmbeddings
except ImportError:
    print("HuggingFaceEmbeddings class not found in langchain.embeddings")

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')
    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import FAISS

db = FAISS.from_documents(docs, embeddings)
print(wrap_text_preserve_newlines(str(docs[0].page_content)))
query = "who is speaking here"
docs = db.similarity_search(query)
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain.llms import HuggingFaceEndpoint

llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.1, max_length=512)
chain = load_qa_chain(llm, chain_type="stuff")
query = "what is this"
docs = db.similarity_search(query)
result=chain.run({"input_documents":docs, "question":query})
print(result)

print(f"Text has been saved to {file_path}")
def query_answer(user_id,query):
    context=extract_info_from_mongodb(user_id)
    data=query+"the following is previous question the user having "+f"user_id"+":"+context
    result = chain.run({"input_documents": docs, "question": data})
    return result







