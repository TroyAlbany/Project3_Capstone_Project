import os
import json
import streamlit as st
import pandas as pd
import numpy as np
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
from streamlit_player import st_player
from PIL import Image

load_dotenv("SAMPLE.env")

# Connect Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Streamlit introduction page
page = st.selectbox("Choose your page", ["Introduction", "NFT Store"]) 

# Page selection box
if page == "Introduction":

    #Introduction page
    st.title(" TOP 10 NFL PLAYS TOKENIZED") 
    st.write("In the 101 year history of the National Football League, there have been many remarkable plays. There have  been plays that made you laugh, plays that made you cry, and plays that just made you scratch your head and wonder why. For the first time, we  bring to you the chance  to own a piece of history. These are the NFL’s all time top 10 plays, and today they can be yours. This limited collection will be offered one time only. Place your bid and become the proud owner of plays that many say will never happen again! We have curated what we believe are the best plays ever. If  you meet the qualifying bid, you can be the proud owner of plays such as The Music City Miracle, or The Catch, and who can forget, one of the greatest plays of all time.....The Philly Special!  The next time someone talks about The Immaculate Reception, you can proudly say you OWN it! Time is running out! Don’t let someone else own what could be yours. Just enter  the store , click on the left, place your bid, and enter a world that few have traveled. Buy 1, 2, or all 10, but act now before it’s too late! Get a token of your appreciation of great American Football. Own it TODAY!")
    
    st.markdown(
        """
        <style>
        .reportview-container{
        background-image: st.image("OIP.jpg");
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("Group 2 Capstone Project")
    st.sidebar.markdown("""
    * **Python Libraries:** pandas, streamlit, streamlit player
    """)
    
    st.sidebar.title("NFT Store")
    st.sidebar.text("GROUP MEMBERS")
    st.sidebar.text("Carl Buchholz")
    st.sidebar.text("Chris Kwiatkowski")
    st.sidebar.text("Edward Schryver")
    st.sidebar.text("Troy Albany")

    #Add images
    image = Image.open('streamlit_code_1.jpg')   
    st.image(image, caption='NFT Purchase code')

    image = Image.open('streamlit_code_2.jpg')   
    st.image(image, caption='NFT Purchase code')

    image = Image.open('streamlit_code_3.jpg')   
    st.image(image, caption='NFT Purchase code')

    image = Image.open('streamlit_code_4.jpg')   
    st.image(image, caption='NFT Purchase code')

    image = Image.open('streamlit_code_5.jpg')   
    st.image(image, caption='NFT Purchase code')

    st.sidebar.text("Issues we ran into while deploying:")
    st.sidebar.text("-Streamlit player installing")
    st.sidebar.text("-Background images not showing up")
    st.sidebar.text("-Speed of flipping between pages")

elif page == "NFT Store":

    #NFT marketplace

    #Background image. Did not show
    st.markdown(
        """
        <style>
        .reportview-container{
        background-image: url("https://cdn5.vectorstock.com/i/1000x1000/22/74/american-football-field-background-vector-5012274.jpg");
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Connect NFTs smartcontract ABI
    @st.cache(allow_output_mutation=True)
    def load_contract():

        # Load the contract ABI
        with open(Path('./top10_abi2.json')) as f:
            contract_abi = json.load(f)

        # Set the contract address (this is the address of the deployed contract)
        contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

        # Get the contract
        contract = w3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )

        return contract
    # Load the contract
    contract = load_contract()

    #contract_address_transact = os.getenv("SMART_CONTRACT_ADDRESS")

    accounts = w3.eth.accounts
    address = st.selectbox("Select Account", options=accounts)


    offer_price = st.sidebar.slider('Offer Price - Eth', 0, 100,)
    st.title("Top 10 NFL Plays of All Time")
    st.sidebar.title("NFT Store")

    st.markdown("""
    This app shows the top 10 NFL plays of All Time as NFT's!
    """)
    
    st_player("https://soundcloud.com/imaginedragons/whatever-it-takes-1")

    #Play 10 purchase contract function
    st.title("Play 10 - Philly Special - Eagles vs Patriots")
    st_player("https://www.youtube.com/watch?v=y3Jqif1TUwQ")

    if offer_price >= 20:
        if st.button("Buy Philly Special NFT"):
            play_10_uri = "https://www.youtube.com/watch?v=y3Jqif1TUwQ"
            tx_hash = contract.functions.mintToken(
                address,
                play_10_uri,
                offer_price,
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000, "to": "0x047D42f1475EafB32FF2f573AA0F272f24eB6606"})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Philly Special NFT"):
            st.error("Offer Price Too Low")
    
    #Play 9 purchase contract function
    st.title("Play 9 - The Minneapolis Miracle - Vikings vs Saints")
    st.image("https://th.bing.com/th/id/OIP._gNH0hiXPzuzAEm027b4OwHaFP?w=213&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    if offer_price >= 20:
        if st.button("Buy The Minneapolis Miracle NFT"):
            play_9_uri = "https://th.bing.com/th/id/OIP._gNH0hiXPzuzAEm027b4OwHaFP?w=213&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"

            tx_hash = contract.functions.mintToken(
                address,
                play_9_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy The Minneapolis Miracle NFT"):
            st.error("Offer Price Too Low")        

    #Play 8 purchase contract function
    st.title("Play 8 - Bart Stars QB Sneak - Packers vs Cowboys")
    st_player("https://www.youtube.com/watch?v=1WXCKG55tlM")

    if offer_price >= 20:
        if st.button("Buy Bart Stars QB Sneak NFT"):
            play_8_uri = "https://www.youtube.com/watch?v=1WXCKG55tlM"

            tx_hash = contract.functions.mintToken(
                address,
                play_8_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Bart Stars QB Sneak NFT"):
            st.error("Offer Price Too Low")

    #Play 7 purchase contract function
    st.title("Play 7 - Immaculate Interception – Steelers v Cardinals XLIII")
    st_player("https://www.youtube.com/watch?v=50M0MOgAAbw")

    if offer_price >= 20:
        if st.button("Buy Immaculate Interception NFT"):
            play_7_uri = "https://www.youtube.com/watch?v=50M0MOgAAbw"

            tx_hash = contract.functions.mintToken(
                address,
                play_7_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Immaculate Interception NFT"):
            st.error("Offer Price Too Low")

    #Play 6 purchase contract function
    st.title("Play 6 - Santonio Holmes game winning TD – Steelers v Cardinals XLIII")
    st_player("https://www.youtube.com/watch?v=rlqipGHuk-4")

    if offer_price >= 20:
        if st.button("Buy Santonio Holmes game winning TD NFT"):
            play_6_uri = "https://www.youtube.com/watch?v=rlqipGHuk-4"

            tx_hash = contract.functions.mintToken(
                address,
                play_6_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Santonio Holmes game winning TD NFT"):
            st.error("Offer Price Too Low")

    #Play 5 purchase contract function
    st.title("Play 5 - Butler picks off Wilson – Patriots v Seahawks XLIX")
    st.image("https://th.bing.com/th/id/OIP.Wd4AvmBwtnwT0uDrf6r_mAHaDv?w=327&h=177&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    if offer_price >= 20:
        if st.button("Buy Butler picks off Wilson NFT"):
            play_5_uri = "https://th.bing.com/th/id/OIP.Wd4AvmBwtnwT0uDrf6r_mAHaDv?w=327&h=177&c=7&r=0&o=5&dpr=1.5&pid=1.7"

            tx_hash = contract.functions.mintToken(
                address,
                play_5_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Butler picks off Wilson NFT"):
            st.error("Offer Price Too Low")

    #Play 4 purchase contract function
    st.title("Play 4 - Music City Miracle – Titans v Bills")
    st_player("https://www.youtube.com/watch?v=Pfz4JViRkoA")
    
    if offer_price >= 20:
        if st.button("Buy Music City Miracle NFT"):
            play_4_uri = "https://www.youtube.com/watch?v=Pfz4JViRkoA"

            tx_hash = contract.functions.mintToken(
                address,
                play_4_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Music City Miracle NFT"):
            st.error("Offer Price Too Low")

    #Play 3 purchase contract function
    st.title("Play 3 - David Tyree Helmet Catch – Giants v Patriots XLII")
    st.image("https://th.bing.com/th/id/OIP.bT29UEGMCg_RBtvekfIsPQHaFD?w=237&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")
   
    if offer_price >= 20:
        if st.button("Buy David Tyree Helmet Catch NFT"):
            play_3_uri = "https://th.bing.com/th/id/OIP.bT29UEGMCg_RBtvekfIsPQHaFD?w=237&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"

            tx_hash = contract.functions.mintToken(
                address,
                play_3_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy David Tyree Helmet Catch NFT"):
            st.error("Offer Price Too Low")

    #Play 2 purchase contract function
    st.title("Play 2 - The Catch Joe Montana – 49ers v Cowboys NFC Championship")
    st.image("https://th.bing.com/th/id/OIP.safFKQlWCAG-NinfB35hWgHaG0?w=168&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")

    if offer_price >= 20:
        if st.button("Buy The Catch Joe Montana NFT"):
            play_2_uri = "https://th.bing.com/th/id/OIP.safFKQlWCAG-NinfB35hWgHaG0?w=168&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"

            tx_hash = contract.functions.mintToken(
                address,
                play_2_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy The Catch Joe Montana NFT"):
            st.error("Offer Price Too Low")

    #Play 1 purchase contract function
    st.title("Play 1 - Immaculate Reception – Steelers v Raiders")
    st.image("https://th.bing.com/th/id/OIP.Tj18qDCd1tM__8cbl7xvWQHaFx?w=230&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7")
    
    if offer_price >= 20:
        if st.button("Buy Immaculate Reception NFT"):
            play_1_uri = "https://th.bing.com/th/id/OIP.Tj18qDCd1tM__8cbl7xvWQHaFx?w=230&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"

            tx_hash = contract.functions.mintToken(
                address,
                play_1_uri,
                offer_price
            ).transact({"from": address, "value": offer_price*1000000000000000000, "gas": 2000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            st.balloons()
    else:
        if st.button("Buy Immaculate Reception NFT"):
            st.error("Offer Price Too Low")

    with st.sidebar.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    # st.sidebar.header('Purchase NFT')
    # st.sidebar.selectbox("Select account", options=w3.eth.accounts),
    # st.sidebar.selectbox("Choose your favorite play!", ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"])
