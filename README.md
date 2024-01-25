##Prerequisites for .ipynb(Colab) file

Create a folder called Data under sample_data and upload ExtractedText.pdf to it

Download the zephyr-7b-beta.Q4_K_M.gguf model from https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/tree/main and add it to the Google drive and mount it.


##Workflow

Information was extracted from websites like radiologyassistant.nl in the form of .md files with a markdown parser.

These .md files were parsed and useful data was extracted from all the .md files and stored in pdf format.

This pdf file was scanned through and the text present in it was divided into chunks.

Gte-embeddings trained on large scale corpuses and embeddings are generated for the chunks created.  These are stored in a vector database.

Zephyr-7b model was used and the vector embeddings generated were passed to it.

This helped in generating responses which were relevant to the context being provided to it.

On entering a query, an appropriate response is obtained.
