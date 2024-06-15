# Mia is excited to explore the Minecraft store and purchase some exciting items for her gameplay. 
# She wants to download the game itself, choose a world to play in, buy some costumes, and maybe even get a farm! Additionally, she’s eyeing some gems to enhance her gameplay. 
# Write a Python program to help Mia calculate the total cost of her Minecraft adventure.

# Mia’s journey through the Minecraft store involves several steps:

# First, she needs to download the game itself, which costs $200.
# Mia will then enter her username and password to access the store.
# Next, she can choose between two worlds: the Survival world for $20 or the Creative world for $100.
# Mia can also browse through three different costume options, each with its own price tag.
# Additionally, Mia has the option to add a farm to her gameplay for an additional $25.
# Finally, she can purchase gems: diamonds for $45, silver for $20, or gold for $30.
# After making her selections, Mia wants to see the total cost of her Minecraft adventure. Let’s create a Python program to help her out.


import streamlit as st
cost = 0
Minecraftcost = 200
survival = 20
creative = 100


download = st.selectbox("Download Minecraft to start",["Choose","Yes $200",'No(Exit)'])
if download == "Yes $200":
    cost += 200
    st.write ("You got minecraft for $200")
    st.balloons()
   
    Name = st.text_input("Type your username: ")
   
    pasword = st.text_input("Type your password: ",type = "password")
   
    world = st.selectbox("Which world do you want to buy",["None","Survival:$20","Creative:$100"])
   
    if world == "Survival:$20":
        st.write("You got survival world")
        cost += 20
        skins = st.selectbox("Choose a skin",["Superman:$20","Sonic:$30","Tails:$20"])
        if skins == "Superman:$20":
            cost += 20
            st.write("You got a superman skin")
       
        if skins == "Sonic:$30":
            cost += 30
            st.write("You got a sonic skin")
       
        if skins == "Tails:$20":
            cost += 20
            st.write("You got a tails skin")
        farm = st.selectbox("Do you want a farm:$25",["No","Yes"])
       
        if farm == "Yes":
            st.write("You got a farm")
            cost += 25
       
        if farm == "No":
            st.write("Thats fine")
       
        gems =st.selectbox("Choose a gem",["Diamonds:$45","Silver:$20","Gold:$30"])                  
   
        if gems == "Dimonds:$45":
            cost += 45
            st.write("You got a diamond")
       
        if gems == "Gold:$30":
            cost += 30
            st.write("You got gold")
       
        if gems == "Sliver:$20":
            cost += 20
            st.write("You got Sliver")
       
        if st.button("Show me cost"):
           st.success(f"The cost is {cost}")
    if world == "Creative:$100":
        st.write("You got creative world")
        cost += 100
       
        skins = st.selectbox("Choose a skin",["Superman:$20","Sonic:$30","Tails:$20"])
        if skins == "Superman:$20":
            cost += 20
            st.write("You got a superman skin")
       
        if skins == "Sonic:$30":
            cost += 30
            st.write("You got a sonic skin")
       
        if skins == "Tails:$20":
            cost += 20
            st.write("You got a tails skin")
        farm = st.selectbox("Do you want a farm:$25",["No","Yes"])
       
        if farm == "Yes":
            st.write("You got a farm")
            cost += 25
       
        if farm == "No":
            st.write("Thats fine")
         
        gems =st.selectbox("Choose a gem",["Diamonds:$45","Silver:$20","Gold:$30"])                  
   
        if gems == "Dimonds:$45":
            cost += 45
            st.write("You got a diamond")
       
        if gems == "Gold:$30":
            cost += 30
            st.write("You got gold")
       
        if gems == "Sliver:$20":
            cost += 20
            st.write("You got Sliver")
 
        if st.button("Show me cost"):
           st.success(f"The cost is {cost}")


if download == "No(Exit)":
    st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw4OEREPEBMSERAQExMSERIQGRkWEBAVFRcWGBYSFRUYKCkgGBoxJxYVITEhJSkrLi4uGh8zODMsNygtLisBCgoKDQ0OGxAQGjclICU3My0tLS0rLTYvMC0tLzctMi0tLS0zKy0tLS0vLysvLi0vLS0tLS0tLS0tLS0tLS0tLf/AABEIAKcBLQMBEQACEQEDEQH/xAAcAAEBAQACAwEAAAAAAAAAAAAABwYEBQEDCAL/xABKEAAABAEECgwMBwACAwAAAAAAAQIDBAUHERIGExYhMTVVcZGSF1FSYXOBhJOys9LhFCIyNDZBVHJ0scTRIzNTgqHCw0KDFSQl/8QAGwEBAAIDAQEAAAAAAAAAAAAAAAQGAgMFAQf/xAA+EQABAgEFCg0EAgMBAQAAAAAAAQIDBAUREjEGEyEyNFFSgaGxFBUWMzVBVHGCkZLB0VNywuGy8CJh8aJC/9oADAMBAAIRAxEAPwC4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADEWWWYuNulAwKLdFKOqZ4Utmfqo9avWdN4vWNTomGq207s3zUx8PhEqWrD3/rap1zli8WoiclGU1tKV/wQuqgt4jMyToSMFYtrnEps5Sdq1JJJqUzqn/V81PXczBZYc55PaHlRukZ8YynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+BczBZYc55PaCo3SHGMp7InpX4FzMFlhznk9oKjdIcYynsielfgXMwWWHOeT2gqN0hxjKeyJ6V+AVjEGeCWHKfV+KntD2o3SPFnGUdckT0r8HmKYlmSU29p/w6FK+tLlKlEnbwmdG+kzo2qB6qPZhRaUMYb5ul63t7L2/qVM+xNSprNnY1ZAzKDJOtXjK84g/KbVtHtltH6xta5HJShxJdIokkiVH6lzodwMiGAAAHW2RygcLCvvlhbbUpNOCtRQn+TIYuWhKSTI4F/jshZ12dZPbCjTBQEVKzhV31GpKDVhO+RYd9Z38xDTDwNVxZZ0R0plkORNwNShV8vZLO8wUoRrsS4p15RuOKOk1K+RF6i3iGlVVVpUscGBDgsRkNKEQ41Uh4bqRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSKpAKRVIBSa+buyFyGiG4ZSqYd9RNmg/JQpXkqSXqv0EecbYT1RaDhz1IGRoLoqJ/m3DTnRLUXVYd1Jyf8AxctnDt3mIqgiSWAiWRqSRZlEZFvGMk/xiUECMvDpqvrsZnX3W+aUU/7KiJBUwAAAzc4mLYr3U9NIwiYp05my6H/eoxZejh8L9QNKc0d5em9X4E+GksporErFHJTtpodS3aTQR1kmdavWooo90ZsYrjmTjOjZErazaa1PXm/6aHYpf9pb1FfcZ3hc5zOU0L6a+aDYpf8AaW9RX3C8LnHKaF9NfNBsUv8AtLeor7heFzjlNC+mvmg2KX/aW9RX3C8LnHKaF9NfNBsUv+0t6ivuF4XOOU0L6a+aDYpf9pb1FfcLwuccpoX0180MtZVY8uTXUMrWlw1tk5SkjIiI1KTRQfujW5lU683y9sshq9raKFowqdrY5YIuPYTENxDaSM1JUhSTNSFJPAdB5j4xk2ErkppIUtntsljLCdDVf90phQ7TYpf9pb1FfcZXhc5F5TQvpr5oNil/2lvUV9wvC5xymhfTXzQ6Gyyw56TUNuKcS6hajQZpI01VUUkR07dCtAwfDVqUnQm6d4ctc5iNoVMOFbTNDA6wAGvscsBfjmExBOpaSo1EklJMzUSTorXt+nQNjYSuSk4ktnyFJYywqquVLaF2HabFL/tLeor7jK8LnInKaF9NfNDhyvN05CMORDkS3VaSajIkKpUfqSV/CZ0FxjxYSolKqbpPP7Y8VsJsNaVwWp8GIGosBobErFXJTt1RxLdpqU1iNVavXooo9w9IzYxXHMnGc2yKrWbTWp681HyaLYpf9pb1FfcZ3hc5zOU0L6a+aDYpf9pb1FfcLwuccpoX0180MjZLIipPfOHUsnDJKV1kkZF41N6g8w1ubVWg7UgljZXBvqJRhoo7jzYxISpRftCVk2ZIUusojMqEmRUUFnBrVctCHkvlrZHCvrkpw0eZrdil/wBpb1FfcbLwuc43KaF9NfNBsUv+0t6ivuF4XOOU0L6a+aDYpf8AaW9RX3C8LnHKaF9NfNBsUv8AtLeor7heFzjlNC+mvmg2KX/aW9RX3C8LnHKaF9NfNBsUv+0t6ivuF4XOOU8L6a+aGFlKEOHedYMyUbTi2zUV4jNJmVJaBqVKFoLDAipFhNiIlFKIvme6QPOoX4hnrEg3GQ1yzJ4n2ruU3VlePoPk/TWNr+cTUV6b+iIvi3IVASSpgAABm5xcWxXup6aRhExVOnM2XQ9e4xZejh8L9QNKc0d5em9X4E+GkspTZmMEZnY+TgkQOsqd09sLX7FMG8qoAAAAAAAASCeHzxn4ZPWOCNGtLrc3kzvu9kP3NJK9qfXCKPxXyro3nEFfLjKnVCC6haDG6OS14TYyWtwL3L8LvK4JJTAAOmsvknw2DeZK+s01m/fTfT8qOMYvbWbQTZulPBpSyItli9y4FPn8Qj6Se+BhVvuNsovrdWlCc6jopzeseolK0GuNFbChuiOsRKfI+iZOg0Q7TbKLyGkJQnMkqKc4molCUHzGNFdFiOiOtVaTkj01k1nflehLUEk/KO2u5ipJCT46T/aQ0R3dRabm5LS50derAnvso8yYCOW0pky+GN5P/sN8DrKrdPZC8X4lNEgqYAEVnVxgrgWv7CJFxi93PZGnep7JpvPz4BzpIHsHGMbosj8SblLMJRRgAAAAAAAA+erKfPYz4h7pqEF2Mp9Lm/JIX2t3IeqQPOoX4hnrEg3GQylmTxPtXcpurK8fQfJ+msbX84mor039ERfFuQqAklTAAADNzi4tivdT00jCJiqdOZsuh69xiy9HD4X6gaU5o7y9N6vwJ8NJZSmzMYIzOx8nBIgdZU7p7YWv2KYN5VQAAAAAAAAkE8PnjPw6escEaNaXW5vJnfd7IYuCilsONvIOhbSkrTnSdNGYaUWjCd2LCbFYrHWLg8z6IkqOREstPo8l1BLLepLAe/6hORaUpPmUeC6DEdDdai0HLHpqPBgCFWfyV4JHOkRUId/GRtULprFxGSv4EOI2hx9CmeVX+StVbUwLq/VB3M0skW2IXFKLxYdNVG+4svVmTTrEM4LaVpIN0cqqQUgpa63uT5XcV0hJKWfh1wkkajOgkkZmZ4CIsJgeoiqtCHz1ZFKhxsS9EHgWrxC2kFeQWgi/kQXOpWk+lyKTJJoDYSdVvf1nXDwlFMmXwxvJ/wDYb4HWVW6eyF4vxKaJBUwAIrOrjBXAtf2ESLjF7ueyNO9T2TTefnwDnSQPYOMY3RZH4k3KWYSijAAAAAAAAB89WU+exnxD3TUILsZT6XN+SQvtbuQ9UgedQvxDPWJBuMhlLMnifau5TdWV4+g+T9NY2v5xNRXpv6Ii+LchUBJKmAAAGbnFxbFe6nppGETFU6czZdD17jFl6OHwv1A0pzR3l6b1fgT4aSylNmYwRmdj5OCRA6yp3T2wtfsUwbyqgAZ+U7M5PhXVsPOmh1FFZNRxVFZJKK+kjI7xkMFiNRaFOjAmmWR4aRIbaUX/AGnd1qcXZDkn9c+bd7I8vrDdxFOGh/6b8jZDkn9c+bd7IX1g4inDQ/8ATfkbIck/rnzbvZC+sHEU4aH/AKb8k7nGlmGjolt2HXXQlkkGZpUmhVdZ0UKIjwGQ0RXI5cBZpkkkaTQHMipQtNNqL1InUZQazslTmhles25BqO+0dsbLbQo/GIsx3/3CRBdgoKfdJJKsRsdEtwL3pZs3FGG8rIAGDnbkq2wyIlJeNDK8aj9NdBHoOqekaYzcFJYbnZVUjrCWx29P6p3dgkkeBwTKDKhxZW1zbrLKmg8xUFxDOG2hpz52lXCJU5yLgTAncnzaaEZnOMbOhLHg8GbKT/EijtZbdTC4eihP7hqjOobQduYZLfpTXWxmHX1fOojAil7AApky+GN5P/sN8DrKrdPZC8X4lNEgqYAEVnVxgrgWv7CJFxi93PZGnep65s41mHjTW84hpFpcTWcUSU0maKCpP13jCEqI6lTKfoMSLJasNqqtKYESnqUq91Ene1w3Oo+4kXxmcp3F0s+k70qcqAlaFiTMmHmnTSVKibWSjSR+s6MA9RzVsU1RZNHgoixGK2nOioc0ZGgADrYqX4JlZtuxDDbiaKyFrSlSaSIypIz3yGKvamBVJMORSmI1HMhqqL1oinpuok72uG51H3Hl8ZnM+LpZ9J3pUh9kbqXIyKWgyUhT7qkqSdKVEazMjIywkIjrVPoMhY5kmhtclCo1Nx+ZA86hfiGesSDcZBLMnifau5TdWV4+g+T9NY2v5xNRXpv6Ii+LchUBJKmAAAGbnFxbFe6nppGETFU6czZdD17jFl6OHwv1A0pzR3l6b1fgT4aSylNmYwRmdj5OCRA6yp3T2wtfsUwbyqgAQucjGcV/09S2IkXGPoMx5BD1/wAlM0NZ1QAAAAAAO0sYlY4KKZiP+KVUOEXrbVeV/F/ORDJrqq0kSXyXhMndC61s70sPoNtRGRGR0kZUkZYDI/WJp80oVMCn6AHriGEOpU2siUhRUKSeAy2jHipSZMe5jkc1aFQ9hD0xPBgCHzjSx4XGrIjpbh/wUbVJeWrTSWZJCJFdS4v8ySW8SVFVMLsK+2zeZcazrgAUyZfDG8n/ANhvgdZVbp7IXi/EpokFTAAis6uMFcC1/YRIuMXu57I071MgNZ2wAKFM3+dFcG30jG6BapWbpuah967iriSU8ACEzi4yis7fVNiHEx1PoUyZDD1/yUzgwOoABz5A86hfiGesSPW4yEaWZPE+1dym6srx9B8n6axtfziaivTf0RF8W5CoCSVMAAAM3OLi2K91PTSMImKp05my6Hr3GLL0cPhfqBpTmjvL03q/Anw0llKbMxgjM7HycEiB1lTuntha/Ypg3lVAAldmdhkoRca++y2lTa7XVM1pSZ1W0JO8e+RiPEhuV1KFvmud5JAkjIcRcKU9S51U6XY7lX9JHOJGF6fmJ/H0h0l8lGx3Kv6SOcSF6fmHH0h0l8lOtlyxeNgEJciEJSlaqiTSoleNQZ0UFmMYuYrbSVJJyk0qcrYS0qmGxTphiTgAAAtU2Ms+FQaW1HS5DHalbZpopbVovftMSoTqWlCn2S3iVK5LH4dfXtw6zXjacYAAAOmsulcoKEefIyrkmq3T63FXk/OnMRjF7qraSbN0l4TKWw+q1e5LT5//AJ3zwnviEfSUAAACmTL4Y3k/+w3wOsqt09kLxfiU0SCpgARWdXGCuBa/sIkXGL3c9kad6mQGs7YAFCmb/OiuDb6RjdAtUrN03NQ+9dxVxJKeABCZxcZRWdvqmxDiY6n0KZMhh6/5KZwYHUAA58gedQvxDPWJHrcZCNLMnifau5TdWV4+g+T9NY2v5xNRXpv6Ii+LchUBJKmAAAGbnFxbFe6nppGETFU6czZdD17jFl6OHwv1A0pzR3l6b1fgT4aSylNmYwRmdj5OCRA6yp3T2wtfsUwbyqgAAAAAAYGeLzVj4gurcGmNYWK5rKH/AG+6EkEYugAAAambiWPBI1CVHQ3Efgr2iM/y1ab37jGyE6hxx58kl/kqqlrcKe+zcW8hLKCeQAAEnndleu83BpPxWStjnvrLxS4k0n+8RozsNBcbnJLVhujra7Anclvmu4nw0llAAACmTL4Y3k/+w3wOsqt09kLxfiU0SCpgARWdXGCuBa/sIkXGL3c9kad6mQGs7YAFCmb/ADorg2+kY3QLVKzdNzUPvXcVcSSngAQmcXGUVnb6psQ4mOp9CmTIYev+SmcGB1AAOfIHnUL8Qz1iR63GQjSzJ4n2ruU3VlePoPk/TWNr+cTUV6b+iIvi3IVASSpgAABm5xcWxXup6aRhExVOnM2XQ9e4xZejh8L9QNKc0d5em9X4E+GkspTZmMEZnY+TgkQOsqd09sLX7FMG8qoAAAAAAGBni81Y+ILq3BpjWFiuayh/2+6EkEYugAAAdhY/JqoyJZh00lbFlSosKUl4ylFvkRGeegetSlUQjSyUNk8B0VepNvUnmfRCcAnHzI8gAAJdO/JFCmo1JXlfgu5ypNtXSKneIR4zestlzcrwOk7vuT39l8ybjQWoAAAKZMvhjeT/AOw3wOsqt09kLxfiU0SCpgARWdXGCuBa/sIkXGL3c9kad6mQGs7YAFCmb/OiuDb6RjdAtUrN03NQ+9dxVxJKeABCZxcZRWdvqmxDiY6n0KZMhh6/5KZwYHUAA58gedQvxDPWJHrcZCNLMnifau5TdWV4+g+T9NY2v5xNRXpv6Ii+LchUBJKmAAAGbnFxbFe6nppGETFU6czZdD17jFl6OHwv1A0pzR3l6b1fgT4aSylNmYwRmdj5OCRA6yp3T2wtfsUwbyqgAdNKFlMnwzimXn0IcRRWSZHSVJEZYC2jIYq9qYFUmwZtlcZiPhsVUXrONdvJXtTehX2Hl8ZnNvE8u+muwXbyV7U3oV9gvjM44nl3012GPnNshg4yHaRDvJdUl4lGSaaSTUWVN8t8hqivaqYDtzFIZRJ4znRWUIqUbUJwNBaQAAAps0Ekfmxqiw/gtZioNauiXEY3wG2qVO6SVYWwE719vcpgkFVAAADrbI5LTGQz0Od43EnVM/8Aisr6FcRkRjFzayUEmRylZNHbFTqXZ17D56cQpJmlRGSkmaVEeEjI6DIxCPpjXI5KUsU/IHoAFMmXwxvJ/wDYb4HWVW6eyF4vxKaJBUwAIrOrjBXAtf2ESLjF7ueyNO9TIDWdsAChTN/nRXBt9IxugWqVm6bmofeu4q4klPAAhM4uMorO31TYhxMdT6FMmQw9f8lM4MDqAAc+QPOoX4hnrEj1uMhGlmTxPtXcpurK8fQfJ+msbX84mor039ERfFuQqAklTAAADNzi4tivdT00jCJiqdOZsuh69xiy9HD4X6gaU5o7y9N6vwJ8NJZSmzMYIzOx8nBIgdZU7p7YWv2KYN5VQAIXORjOK/6epbESLjH0GZMgh6/5KZoazq0ABQAAAAAftlpTikoQVKlqJKS21KOgi/kDxzka1XOsTCvcfQ0gyYiDh2YdOBtBEZ7pWFSuMzM+MTmpQlB8ylUodKIzoq9a/wDE1IdgPSOeKQB5AAARadCR/Bow3UlQ3FEbm8ThUE4XRV+4xEitodSXqYJVfpNUW1mDV1fGox41ncAApky+GN5P/sN8DrKrdPZC8X4lNEgqYAEVnVxgrgWv7CJFxi93PZGnepkBrO2ABQpm/wA6K4NvpGN0C1Ss3Tc1D713FXEkp4AEJnFxlFZ2+qbEOJjqfQpkyGHr/kpnBgdQADnyB51C/EM9YketxkI0syeJ9q7lN1ZXj6D5P01ja/nE1Fem/oiL4tyFQEkqYAAAZucXFsV7qemkYRMVTpzNl0PXuMWXo4fC/UDSnNHeXpvV+BPhpLKU2ZjBGZ2Pk4JEDrKndPbC1+xTBvKqDAEKnIMv/JxX/T1LYiRcY+gzHkEPX/JTNVi2yGqlDrUKKxbZBSgoUVi2yClBQp5Ix6AB4bSauSLfF29ReJDJrbxuKpJBdI+IhtgtpdScG6CVXqT3tLX7kt9k8yykJRRzwowBgbD7LPCpRi2lKpbd8aH2qGvFvZy8biGlj6XKWKcpsvEihPRP8kxvFh2LgN+NxXQAMtOLI/hcE4aSpcY/GRRhOr5SSzppvbdA1xW0tOtMsq4PKkpsd/iuuzaQ8RD6AABTJl8Mbyf/AGG+B1lVunsheL8SmiQVMACKzq4wVwLX9hEi4xe7nsjTvUyA1nbAAoUzf50VwbfSMboFqlZum5qH3ruKuJJTwAITOLjKKzt9U2IcTHU+hTJkMPX/ACUzgwOoABz5A86hfiGesSPW4yEaWZPE+1dym6srx9B8n6axtfziaivTf0RF8W5CoCSVMAAAM3OLi2K91PTSMImKp05my6Hr3GLL0cPhfqBpTmjvL03q/Anw0llKbMxgjM7HycEiB1lTuntha/Ypg3lVAA/BtJO+ZEecgPayoLSjcp0EB7WXOLSjcp0EArLnFpRuU6CAVlzkinfSRRjJERF/66cHCOCNGtLnc2tMmd93shhhpLCXOb2R/BIJslFQ49+M5tkavJTxFQWkS4baGnz2eJVwiVOVLEwJq+VNMNhyzNTgyv4JBOmk6HHfwW9sjXhMsxVjGuI6hp1JnkvCJW1FsT/JdXypFpJjlQr7UQjC0tKqNsiwp4ypLjERq0LSXyUwEjwnQ3f/AElH91n0TCvpdQhxB0pWklJMvWSipI/5E8+YvY5jla61MCntAxPCipIAfP8AZdJJwUW8zRQimu1tVF30kWa+niEJ7arqD6RNsq4TJmxFtsXvT+06zpxiTimTL4Y3k/8AsN8DrKrdPZC8X4lNEgqYAEVnVxgrgWv7CJFxi93PZGnepkBrO2ABQpm/zorg2+kY3QLVKzdNzUPvXcVcSSngAQmcXGUVnb6psQ4mOp9CmTIYev8AkpnBgdQADnyB51C/EM9YketxkI0syeJ9q7lN1ZXj6D5P01ja/nE1Fem/oiL4tyFQEkqYAAAZucXFsV7qemkYRMVTpzNl0PXuMWXo4fC/UDSnNHeXpvV+BPhpLKU2ZjBGZ2Pk4JEDrKndPbC1+xTBvKqAAAAAAAAEgnh88Z+HT1jgjRrS63N5M77vZDP2HST4bGMsmVKCO2O+4i+ZHnvFxjWxtZ1B0pzlXBpM56W2J3r/AGkvySE0+cHkAR6diVrdFJh0n4kMnxto3F0GegqpcZiLGdS6gu1z0lvcnWKtrtyfK07DDjUWAsc1MrW+ENhR0rhlVd+oqk0H0i4hKgupSgo10ElvUpviWOw60t9lNsNpwgAJ9O5JFsZbi0l4zB1F77azvHxHRrGNMZuCkslzkqqRXQFsdhTvT5TcScRi5FMmXwxvJ/8AYb4HWVW6eyF4vxKaJBUwAIrOrjBXAtf2ESLjF7ueyNO9TIDWdsAChTN/nRXBt9IxugWqVm6bmofeu4q4klPAAhM4uMorO31TYhxMdT6FMmQw9f8AJTODA6gAHPkDzqF+IZ6xI9bjIRpZk8T7V3KbqyvH0HyfprG1/OJqK9N/REXxbkKgJJUwAAAzc4uLYr3U9NIwiYqnTmbLoevcYsvRw+F+oGlOaO8vTer8CfDSWUpszGCMzsfJwSIHWVO6e2Fr9imDeVUAAAAAAAAJDPD54z8OnrHBGj2l1ubyZ33eyHfTRyRa2Fxai8Z86qKf00HRTxnToIZwW0JSc26OVV4yQUsbb3r8IUAbiuHFlSORDMuvr8lpClnv0FTQW/6h4q0JSbYEF0aI2G21VoPnWLiFvOLdWdK3FKWo99R0n8xBppwn06HDbDYjG2JgTUeoDM083UreCxrZGdCH/wAFe1SryD00FxmM4TqHHInuS3+SqqWtwpqt2bi4kJhQDyAONKUIiIacZWVKHUmhWZRUUjxUpSg2QoroT0iNtTCfO0fCLh3XGV+W0tSFb9B4c3r4xCVKFoPp0GM2NDbEbYqUlFmXwxvJ/wDYboHWVm6eyF4vxKaJBUwAIrOrjBXAtf2ESLjF7ueyNO9TIDWdsAChTN/nRXBt9IxugWqVm6bmofeu4q4klPAAhM4uMorO31TYhxMdT6FMmQw9f8lM4MDqAAc+QPOoX4hnrEj1uMhGlmTxPtXcpurK8fQfJ+msbX84mor039ERfFuQqAklTAAADNziF/8ANivdT00jCJiqdOZsth/3qMWn0cPhfqBpTmjvL03q/Anw0llO4sfslipPtng5oK21a1dNbyaaKNryjGTXq2wgy2boErovtOCyhc53GyTKm6Z1O8ZX15C5PyLMvn+hskypumdTvC+vHJ+RZl8/0NkmVN0zqd4X145PyLMvn+hskypumdTvC+vHJ+RZl8/0NkmVN0zqd4X145PyLMvn+hskypumdTvC+vHJ+RZl8/0dDL8uREoOJdfNJrSioRoKqVWkzwcZjBzldadCRyKFJGqyHYq04VpO3grPpQYbQy2bJIbSSElUwERUF6xlfXIQosxySI9XuppXCuH9Hv2SZU3TOp3j2+vMOT8izL5/o4EtWZx0a0bDykWtRpNRITVM6pkZFTTgpIh4sRypQpIks0SWTREiw0WlM65zPDA6YAHkjMqDIzIyvkZYSPbLfAKlOA1yZyJUIqKzXGi/8xsvrziLc/Isy+f6POyTKm6Z1O8L68cn5FmXz/Q2SZU3TOp3hfXjk/Isy+f6M5LEpuxjqn3atsWREo0FVI6pUEdG2MFVVWlTpyWTMk0NIbKaEzqcqx+ySKk62eDmgrbUr101vIrUUbXlGPWvVthplk3wZXVvtOCmihc//DudkmVN0zqd4yvryFyfkWZfP9DZJlTdM6neF9eOT8izL5/oz0tSs9Gum+8aTWaST4pVSoKmi9xjBXK5aVOlJZLDksO9w7LcJwB4SQAO1kCyCJk9S1w5oI3CJKq5VrxHSVGkZNcrbCHLJDBlbUbFpwZlO72SZU3TOp3jK+vIHJ+RZl8/0NkmVN0zqd4X145PyLMvn+jNSrKLsW8uIdoNxyg1VSoTeSSSoLMRDBVpWk6smk7JPDSEyxP+nEHhuAA58gedQvxDPWJGTcZCNLMnifa7cpurKsfQfJ+msbH84mor039ERfFuQqAklTAAADgy3AFFQ70Od4nW1Ip2jMrx6aB45KUVDfJoywIzYqdS0k5sJWh1mKkSK/DcM11CPDTerEW2ZGRKLbIzGiHhRWKWedUcyLDnGBhTBT/cypg/0pjpasei4JZodbVQR3nEkZtrLbJRfLCNTmq207kll8nlLazHalXCmo621q3KtBjEl1m59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59otatyrQYCs3PtFrVuVaDAVm59p5JlZ/wDFWqYHldudPNDcWB2KupdTHRZGyxD0uJtnimtRFeUZHgSWGk9ohuhsWmspXp4nNisWTQFrOdgwYaP9d6nOsbplWV3I4iPweH8gz9dCTS2Wfyl7w9b/AJvpNEtokE2tk3/263evshUBIKmAAAAAZWy2wxuPMnm1WiKRRVdTgVVwVqL9JepRXy3xrfDrYUtOtN07PkqXt6VmLanx8HUMRtkkKVrch2osivE4SirHnMjIz40jGmInVSTHQZmjrWbEVn+qP0u89t0MvZNTrd4V36J5wGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFd+iOAzX2jYLoZeyanW7wrv0RwGa+0bBdDL2TU63eFeJonnAZr7Rs/RxX5DlqVTJMatELD0kZtN0GpVG2RGdJ+8q9tDyq99uA3Mls2yDDJ0V786/wBTYms3EjSSxBtJZZTVQnjUo/WpR+sxuaiNShDgSiUxJREWJEWlV/tCHOHpoAAAAAAA8UADyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/Z",width=1000)  




