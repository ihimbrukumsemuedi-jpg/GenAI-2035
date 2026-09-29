from core.ingestion import load_documents, load_and_split_folder

output=load_and_split_folder('docs')
print(output)
