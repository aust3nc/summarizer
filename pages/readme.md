1) Input Imbedding (a word imbedding layer produces a lookup table of learned vectors representing each word; each word maps to a vector with continuous values)
   
2) Positional Encoding (add information about the position of each input in relation to the rest of the input); for every odd timestep, create vector via cosine func; for every even timestep, create a vector via sine func. Finally, perform vector addition to combine position vector with its accompanying lookup table vector. Now, each element in the input sequence, including accompanying information regarding position, is 'hashed' into a vector of continuous values.
   
3) Encoder Layer -- map input sequence into abstract representation which preserves learned information respective to the entire input sequence. It comprises two sub-modules: multi-headed attention and a fully connected network. These sub-modules are residually connected and feed computed representations through a normalization layer. 
   A) Multi-Headed Attention: applies Self-Attention, which allows the model to associate each input element with each other input element. Intuitively, self-attention (think of this as attention regarding one's context) would allow the model to form associations between elements and hash the compounded/contextual value. Given the input sequence 'How are you?', self-attention would teach the model that 'you' is associated with 'are' and 'how'. Additionally, the model would learn that the confluence of each encoded vector equates to a question, in terms of semantic structure. Multi-headed attention is achieved by:

        I) feeding input into three fully connected layers which output query, key, and value vectors, respectively. An intuitive explanation: a streaming service takes a *query* as an input, i.e., 'action movies', maps this against a set of *keys*, i.e. 'Transformers', 'James Bond', etc., and returns best match movies as *values*. 

        Query, key, and value matrices are split into n-vectors before applying self-attention. 

        // go into more theory here; this is not explained well enough (bring it back to the actual methodology; this basal intuition isn't enough lol)

        II) Self-attention: each n-set of vectors is passed into a self-attention 'head'. This allows each head to output a vector with different learned information. Before going through a final linear layer, output vectors from each head are concatenated into a single vector, which serves as input for a linear layer. Here is how self-attention is done for each head:
        
            a) For each n-set of vectors, *Queries* and **keys* pass through a dot product multiplication function to produce a *score matrix*, which determines how much precedence an element possesses respective to every other element. Queries are then scaled by element-wise division by the square root of the dimension of the queries and keys, which allows for stable gradients (eliminating the exploding gradient problem, which can occur when multiplying values). 
            
            b) Next, an element-wise softmax function is applied to the scaled score matrix, which makes higher scores higher and lower scores lower, outputting attention weights between 0 and 1 (intersection 0,1). The outputted attention weights give the model confidence in deciding which elements to attend to more. 

            c) Then, attention weights are dot-multiplied by *values*, outputting a vector with higher output values for more important word values, and lower output values for less important word values. 

            d) Finally, this output vector is concatenated with the other output layers then fed into a linear processing layer, which helps the model learn correlations between input and output (i.e., weights in the output vector will be negative if input and output are negatively correlated, positive if weights are positively correlated, and 0 if inputs and outputs are fully independent). 
        
            e) Because each head's output vector in theory learns different information, the encoder module possesses better representation power than a single attention mechanism alone.

            f) In summary, multi-headed attention is a module in a transformer network which computes attention weights for the input and produces an output vector with encoded information concerning how each word relates to other words in a given sequence. 

    B) Residual Connection, Layer Normalization, and Pointwise Feed Forward:
        I) The multi-headed attention output vector is added to the original input, creating a residual connection. 
        II) The output of the residual connection goes through a layer normalization layer.
        III) The normalized residual output is passed into a pointwise feed forward network, which is comprised of a ReLu activation function sandwiched between two linear layers. 
        IV) The output is then added to the input of the pointwise feed forward module; overall:
            a) residual connections allow for better training by creating a free and direct flow of gradients through the network. 
            b) layer normalizations stabilize the network, reducing training time. 
            c) the pointwise feed forward module, as a whole, processes input vectors to produce potentially richer representations of input sequences.

    C) Note: the purpose of the encoder layer is to teach the next module, the transformer decoder, relationships to pay attention to. Additionally, the encoder layer may be stacked n times to further encode information, helping the model learn more diverse attention representations, potentially boosting the predictive power of the entire transformer network. 

4) Decoder Layer -- Generate Text Sequences by employing similar sub-layers as the encoder, including two multi-headed attention layers, a pointwise feed forward layer, and residual connections with layer normalization following each sub-layer. Although the mechanisms of these sub-layers are similar to the mechanisms of encoder sub-layers, they have different jobs. Each multi-headed attention layer has a different job, and is capped with a linear classifier layer and a softmax which outputs word probabilities. The decoder is auto-regressive, taking both previous decoder outputs and encoder outputs as inputs. The decoder knows to halt once an n-token output has been generated. Let's dive in.
   
    A) Output Embedding and Positional Encoding fed into -> 
    B) first Multi-Headed Attention sub-layer - outputs masked values
        I) The decoder is auto-regressive, generating the sequence word by word, meaning it needs to be prevented from being conditioned by future tokens (i.e., each generated element should only have access to the elements generated before it, but not after). The mechanism used to keep the decoder's first multi-headed attention layer from computing the attention of future elements is:
            a) Masking!!! A look-ahead mask is applied before calculating soft-max and after scaling scores. 
            b) The mask is a matrix the same size of the attention scores, but it's filled with zeroes and negative infinities. 
            c) After adding the look-ahead mask to scaled attention scores, we get an output matrix of masked scores, the top right triangle of which is filled with negative infinities.
            d) After applying softmax to this masked score matrix, the output matrix 0s out future scores, leaving only a triangle of attention weights behind. 
            e) This ensures that the model will not take future generated elements into account. This masking function is the ONLY DIFFERENCE between the first multi-headed attention decoder sub-layer and the multi-headed attention encoder sublayer.
            f) As in the encoder layer, multi-headed outputs are concatenated and fed into a linear layer. 
        II) The output of the first multi-headed attention layer is a masked vector with information concerning how the model should treat the decoder's input. 
    C) second Multi-Headed Attention sub-layer - takes queries and keys from the encoder, which are matched to the first multi-headed layer's output values. 
        // need more information here; knowledge gap!
        I) This matches the encoder's input to the decoder's input, allowing the decoder to decide which input elements (encoder or decoder) to focus on. Think of this as attention reinforcement. 
        II) The output of the second multi-headed attention sub-layer is passed through a pointwise feed-forward layer. 
    D) Linear Classifier - takes feed-forward output and outputs
        I) The classifier is as large as the number of classes in the input. If we have 10,000 classes for 10,000 words, the output of the linear classifier will be of size 10,000. This output is fed into a softmax layer.
    E) Softmax Layer - outputs probability scores between 0 and 1 for each class. The index of the highest probability score is a predicted element. (i.e., for each class, (className: probabilityScore)[sharedIndex]
    F) The decoder recursively grabs the softmax output and adds it to a que of decoder input, continuing to decode until n-token is predicted. N is equal to the number of classes. 
    G) The decoder may be stacked n-layers high, with each layer taking inputs from the encoder and previous decoder layers, iteratively learning to focus on different combinations of attention, boosting predictive power. 



    


