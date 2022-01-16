import streamlit as st

map_e_to_d = {
    'a':'q',
    'b':'g',
    'c':'p',
    'd':'n',
    'e':'o',
    'f':'z',
    'g':'t',
    'h':'v',
    'i':'e',
    'j':'s',
    'k':'y',
    'l':'x',
    'm':'u',
    'n':'d',
    'o':'w',
    'p':'c',
    'q':'a',
    'r':'j',
    's':'r',
    't':'b',
    'u':'m',
    'v':'f',
    'w':'i',
    'x':'l',
    'y':'k',
    'z':'h',
    ' ':' '
} ## Random Manual mapping
map_d_to_e = {

} ## Inverse Mapping

def gen_inv():
    '''
    Inverting the encryption map
    '''
    if len(map_d_to_e)==0:
        for e, d in map_e_to_d.items():
            map_d_to_e[d]=e

def encrypt(x):
    '''
    Encrypts the input based on table lookup
    '''
    out = ''
    try:
        for c in x:
            sub = map_e_to_d[c.lower()]
            out += sub.lower() if c.islower() else sub.upper()
        return out
    except KeyError:
        st.warning("Input character out of encoding dictionary")
        return x

def decrypt(x):
    '''
    Decrypts the input based on table lookup
    '''
    gen_inv()    
    
    out = ''
    try:
        for c in x:
            sub = map_d_to_e[c.lower()]
            out += sub.lower() if c.islower() else sub.upper()
        return out
    except KeyError:
        st.warning("Input character out of decoding dictionary")
        return x

st.title('Encipher / Decipher')
level = st.slider("Do you want to decipher it?", 0, 1)

input_string = st.text_input('Enter the message')
# crypt = st.text_input('Enter the encrypted message')

result = ''
if input_string!='':
    if level == 0:
        result='encrypted version is \n','**' + encrypt(str(input_string)) + '**'
    elif level == 1:
        result='decrypted version is \n', '**' + decrypt(str(input_string)) + '**'
# if crypt!='':
#     result='decrypted version is ' + str(crypt)

if result!='':
    st.text(result[0])
    st.markdown(result[1])

if st.checkbox("Show Mapping"):
    if level == 0:
        st.markdown("<br/>".join([ "`"+k+"->"+v+"`" for k, v in map_e_to_d.items()]), unsafe_allow_html=True)
    elif level == 1:
        gen_inv()
        st.markdown("<br/>".join([ "`"+k+"->"+v+"`" for k, v in map_d_to_e.items()]), unsafe_allow_html=True)
