ADD COLLAPSIBLE CODE, LATEX MATH TO EACH SECTION!
CREATE TABLE OF CONTENTS! 
ADD PICTURES!

notes:
bert produces context-dependent embeddings, utilizing neighboring words to capture nuanced semantic relationships, i.e., 'The game will lead to a tie if both the guys tie their final tie at the same time' will produce 3 different, context-dependent embeddings for the word 'tie'. The disadvantage here is that we need the large pretrained language model each time behind our custom layer rather than simply training our model on a text corpus once, as is the convention of other models, such as Word2Vector and GloVe. 

Transformer encoder cells read input sentence, decoder cells predict output sentence word by word, but BERT only needs the encoder, which reads the input features then derives features for NLP tasks. BERT is bi-directional because it reads all input words simultaneously. 

BERT Large utilizes 24 encoder blocks, 16 attention heads, 340 million parameters, and outputs a size of 1024 dimensions. 

F1 score of humans is 91.2%; F1 score of BERT is 93.16%. 

BERT was trained on a corpus of unlabelled text including all of Wikipedia. Training on this corpus was accomplished via both Masked Language Model (MLM) and Next Sentence Prediction (NSP).

In MLM, the model is fed a sentence with 15% of the words masked; the challenge is for BERT to correctly predict the masked words corectly given the context of unmasked words. 

In NSP, the model is fed 2 sentences; it is supposed to return 1 if the first comes after the second and 0 if the second comes after the first. 

Self-attention in the encoder: the input sequence pays attention to itself.
Self-attention in the decoder: the target sequence pays attention to itself. 
Encoder-Decoder attention in the Decoder: the target sequence pays attention to the input sequence. 

Attention heads perform in parallel; the concatenation of their output vectors teaches the model multiple nuanced relationships per word.

ENCODER SELF-ATTENTION: Input seq is fed to input embedding, position encoding; these return encoded representations for each input element, capturing position and meaning. These are fed to query, key, and value, returning encoded representations with attention taken into account. 

DECODER SELF-ATTENTION: The target sequence is fed to the output embedding and position encoding sub-modules, producing encoded representations for each word which capture context and meaning. This is fed to query, key, and value, which incorporates attention scores. After passing through layer normalization, these representations are fed to the Query parameter in the encoder-decoder attention in the first Decoder layer.

Decoder Encoder-Decoder Attention and Masking: Takes a representation of both the target sequence (from decoder self-attention) and a representation of the input sequence (from the encoder stack), producing a representation of the target sequence with attention scores which also capture the influence of attention scores from the input sequence from the encoder. In short, encoder-decoder attention in the decoder computes the interaction between each target word with each input word. "Therefore each cell in the resulting Attention Score corresponds to the interaction between one Q (ie. target sequence word) with all other K (ie. input sequence) words and all V (ie. input sequence) words. Similarly, the Masking masks out the later words in the target output."

Query, Key, and Value are each assigned multiple heads. There aren't just 3 heads lol. 

Encoding batches from embedding and position encoding sub-modules are fed to a linear layer as a matrix with sampleCount height, numEmbeddings breadth, and sequenceLength width. the output becomes input for self-attention encoder (value,key,query)  

The linear layer output is logically split; a single matrix is fed into the key, query, and value parameters with logically separated sections of the matrix for each attention head. Each attention head shares the same linear layer but operates on its own logical section of the input matrix. 

Logical partitioning is achieved by deriving the query size from the dividend of embedding size and number of heads; thus, we return a 'stack' of logically separated layer weights for each head to process. 


# A collapsible section with markdown
<details>
  <summary>Click to expand!</summary>
  
  ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets
</details>

  <details>
  <summary><b><u>Top Level Toggle</u></b></summary>

  <p>
          Great, Top Layer summary text working fine.
  </p>

  *   <details>
      <summary><b>Mid Toggle</b></summary>

      <p>
          Great, Middle Layer summary text working fine.
      </p>

      * <details>
        <summary><b><i>Inner Toggle 1</i></b></summary>

        <p>
          Great, Inner Layer summary text working fine.
        </p>

      </details>

      * <details>
        <summary><b><i>Inner Toggle 2 - should not show up when Mid Toggle is collapsed :(</i></b></summary>

        <p>
          Great, Inner Layer summary text working fine.
        </p>

      </details>
  </details>
  </details>

Additional topics to cover: 
computation/processing required for this large language model
advantages over lstms/grus (reference window as large as is computationally feasible vs. limited lstm/gru reference window. i.e., more state.)