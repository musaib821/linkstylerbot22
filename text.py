from load_data import * 
#VERSION="2.0.2"
intro2="Hey There! 👋 Welcome To The Link Styler Bot 🤖. My Name Is [Insert Bot Name Here], And I'm Here To Help You Make Your Links Pop 💥. Want To Give Your Channel A Fresh Look With Some Customized Links And Buttons?" 
setting="This Bot Is Easy To Understand😀 \n •) Set The Title For Your Message\n •Change Style Using ⚙️ \n •) Your Data Is Not Stored Anywhere So You Have To Set These Values Everytime To Use Me ♻️"
row_num="•Defaut is Set To 2 Buttons In Row \n •) Currently We Support Only 2 Buttons In Row,It Will Be Increased In Next Update \n •) HTML links Will Be Available In Next Update \n Join Channel To Receive New Updates 🌟"
links_txt="💡 You Can Send {} Any Photo With Links In Caption Or Any Text With Links \n Use /help To Access Help Section"
starting_message="👋 Hey There {}! \n 👉 This bot can convert multiple links into Telegram buttons  \n 👉 Supports channels and inline mode also  \n 👉 Use /commands to access available commands \n 👉 For complete details about bot use /help " 
next_1="👉Click On Customize Links To Customize You Links 🔗 \n👉 For More Info You Can Go To Others  "
next_2="👉 Row Width : Number Of Buttons In Row \n👉 Title : Text In Message \n👉 Label : Label On Buttons-Premium"
next_78="👉Set Row Width \n👉 Default Is Set To 2 \n☛ 1,2,3 Are Available In Free Plann \n👉  Join Premium To Use Others \n☛ HTML Links Are Not Supported Yet "
next_3="🎉 Set Row Width \n👉 Default Is Set To 2 \n👉 1,2,3 Are Available In Free Plan \n👉 Join Premium To Use Others 💰 \n ❌ HTML Links Are Not Supported Yet 🚫"
next_4=" Set Title  📌 \n👉 Your Next Message Will Be Treated as a Title For Message 🔖 \n👉 Title Should Be In One Message 🚨"
next_5="Set Label \n👉 Your Next Message Will Be Treated As A Label \n👉 label Must Be In One Message Only " 
abobut=f'╒═════════════════════✰°\n ➥ BOT NAME:- Link Styler Bot \n ➥ USERNAME :- @linkstylerbot \n ➥ LAUNCH DATE :-  \n ➥ LAST UPDATED:-12-2-2003 °✰═════════════════════╛'
about="╭─────────────────────╮\n      ❝𝙱𝚄𝚃𝚃𝙾𝙽𝙸𝚉𝙴 𝙱𝙾𝚃❞ \n      ➥ LAUNCH DATE :- {}\n      ➥ LAST UPDATED :-{} \n      ➥ DEVELOPER :- @devsavior\n      ➥ TOTAL USERS :- {}\n      ➥ <a href='https://t.me/BotsArchive/2721'>FEEDBACK</a> \n      ➥ VERSION :- {} \n      ➥  <a href='{}'>FAQs</a>\n╰─────────────────────╯"

account='''╭┈➤ ❝ [{}]
 ➥ CURRENT PLAN :- {}
 ➥ PURCHASE DATE :- {}
 ➥ EXPIRY DATE  :- {}
 ➥ CHANNELS ADDED  :-  {}'''
acunt="┏━━━━━━ ⋆⋅☆⋅⋆ ━━━━━┓\n┃ PLAN :- {}┃\n┃ PURCHASE DATE:-{}┃\n┃ EXPIRY  DATE :-{}┃\n ┃CHANNELS LINKED :- {} \n┗━━━━━ ⋆⋅☆⋅⋆ ━━━━━┛"
next_6="\n👉 Unlock Premium Features and Enjoy The Best Of This Bot \n👉 VISIT FAQs For Better Understanding This Bot \n👉 For More Queries and Bugs Please Use Support Button \n👉 Thanks For Using This Bot"
rate="https://t.me/BotsArchive/2721" 
premium="Premium Version Is Just Launched To Keep This Bot Running!! \n👉 You Can Enjoy Premium Features at just 30rs per month (1rs/day) or get a discount at 100rs for 5 months (0.6rs/day) \n👉 Indian Users Can Pay With UPI and Rest Can Use Stripe Or Crypto \n👉 "
crypto="BTC:<code> bc1q8s8pq8880659rsufmnfmqpcdh554qag5xcvhya</code> \n👉 ETH:<code>0x750C9976c988BE7E233EF6c2579e8d0C22F84019</code> \n👉 DOGECOIN :<code>DQPL7SrAJVWxALufeBsLvKbYmEngrzzJcQ</code> \n👉 Please Pay Either For 1 month Or 5 Months "
devcom="Available Commands \n /add_pro Add User In Premium Members \n /add_channel Adds Channel In Premium \n /get_users get total users \n /post Post To Users \n Total User:Not Defined \n "
faq="📊 <b>Frequently asked questions </b> \n 1. Why are some links not detected? \n 2. How Does The Bot Work With Channels? \n 3. What is the premium plan and what are its benefits?? \n 4. How can I Cancel and request a refund for my premium subscription \n 5. Can I Get A Free membership? \n 6. Inline Mode? \n"
#faq_1="While The Bot Is Designed To Detect Every Link In Message There m"
faqyys={
    'faq_1':"<b> Why are some links not detected? </b> \n <i> There might be instances where the bot is unable to detect certain links. Here are some solutions you can try: \n 1. Use https:// before each link \n 2. Add a space before each link \n 3. Validate the format of link \n If you are still facing issue contact me at @ezy_dev </i>"
   ,'faq_2':"<b>How does bot work with channels</b> \n <i> You can post direct in channel. \n Just add the bot in channel  \n use /add_channel to add channel \n use /remove_channel to remove channel \n You Can add upto 2 channels in free plan .\n Premium users can add upto 5 channels </i> "
   ,'faq_4':"<b> Can i cancel and request a refund for my Premium Membership? </b> \n <i> if our premium services do not meet your expectations, you can cancel your subscription at any time. \n We want to ensure that you are fully satisfied with the services you receive.\n To cancel your premium membership contact the developer \n Please Note That Based on the refund policy, you may receive only half of the payment back </i>"
   ,'faq_3':"<b>What is the Premium Membership and what are its benefits? </b> \n <i> Premium Membership is launched to offer enhanced functionality and exclusive benefits to users.\n Funds generated from Premium Memberships are utilized to cover server costs, ensuring a reliable and uninterrupted service for all users. </i> \n<b>Premium Membership Benefits </b>  \n <i> Unlimited Number of Links \n 20 Edits per Message: ✏️ \n Support for Up to 5 Channels: 📢 \n Adding Custom Channel Button ✅ </i>"
   ,'faq_5':" <b> Can i get a free Premium Membership? </b> \n <i> We occasionally offer discounts and free membership coupons. \n use /offers to check available coupons. \n Stay tuned to our official channels to be notified about any ongoing offers. </i>"
   ,'faq_6':"<i>This Bot Can Work With Inline Mode also \n Use it to create  buttons in any chat just type @buttonize With First parameter as Label second as link and third as a heading of message</i>"}
upi_text="UPI:<code>devsavior@axl</code> \n Either Pay For One Month Or 5 Month \n After Payment Is Done Send Screenshot " 
tutorial='''@buttonizebot
 ⚡️Supporting photos,videos and text content 
 ⚡️Supporting instant link conversion 
 ⚡️Configure settings before sending links
 ⚡️Works in inline mode and channels also
    Access /commands '''
commands='''Available Commands 
☞ /create_buttons - configure settings before sending links
☞ /add_channel - add channel 
☞ /remove_channel - remove channel 
☞ /account - access your account
☞ /premium - buy premium membership 
☞ /support - chat with admin 
☞ /offers - to check available offers
☞ /send_proof - send payment proof 
☞ /settings - 🆕 set default settings
☞ /cancel - cancel any ongoing Process''' 
others_text='''@buttonizebot ✨
  Join channel for more Info 
  Report bugs at @ezy_dev or /support 
  Improve this bot by giving your feedback ✍🏻
  Check /offers for exciting offers 
  Visit FAQs for more info 📝
''' 
topi='Select One Channel Where You Want To Post '
buy_pro_df='''Introducing our Exclusive Premium Plans!

1 Month Plan: 30rs 
3 Months Plan: 80rs
6 Months Plan: 150rs
12 Months Plan: 320rs
<b>Payment Methods</b>
  <b> Indian Users </b>
 UPI :- <code>devsavior@axl </code>
 <b> Others </b>
  <a href='https://buy.stripe.com/bIY4jH4x72xmaFW148' >STRIPE</a>
<b> CRYPTO PAYMENT</b>
BTC :- <code>bc1q8s8pq8880659rsufmnfmqpcdh554qag5xcvhya</code>
TRX :-<code> TPT7W5Cnc6svar5S8BnC5ssRmcC8fKZYLj </code>
ETH:-<code>0x750C9976c988BE7E233EF6c2579e8d0C22F84019</code>  

AFTER PAYMENT PLEASE SEND PROOF using /send_proof or at @devsavior'''