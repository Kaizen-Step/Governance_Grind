# Libraries
import streamlit as st
from PIL import Image


# Layout
st.set_page_config(page_title='Governance Grind',
                   page_icon=':bar_chart:', layout='wide')
st.title('Governance Grind')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/3.png'))
with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""# 🌔Terra (Governance) #""")

st.write("""
Terra is a blockchain protocol and payment platform used for algorithmic stablecoins. The project was created in 2018 by Terraform Labs, a startup co-founded by Do Kwon and Daniel Shin. It is most known for its Terra stablecoin and the associated Luna reserve asset cryptocurrency.  In May 2022, the Terra blockchain was temporarily halted after the collapse of the stablecoin TerraUSD (UST) and Luna, in an event that wiped out almost USD45 billion in capitalization within a week. 
### Goveranance In Terra ###
Here, ‘governance’ refers to decision making and control, with a focus on who has these capabilities.
A compulsory requirement for a Blockchain project’s success is that it maintains decentralisation. The project must also create governance that can deal with the complexity in decision making in order to reduce uncertainty, delays and costs when used by stakeholders over existing systems.
Governance becomes more complicated when you have many stakeholders within a particular blockchain network. Public Blockchain networks, therefore, have much higher governance risk than private Blockchain networks. Anyone who joins a public blockchain may in some way affect and vote in the system.
The Terra protocol is a decentralized public blockchain governed by community members. Governance is the democratic process that allows users and validators to make changes to the Terra protocol. Community members submit, vote, and implement proposals.The governance module maintains the logic for all governance activity.
To learn how to vote with staked Luna or submit proposals, visit the [Station governance guide](https://docs.terra.money/learn/station/governance/).

### Drafting and submission ###
Proposals start as ideas within the community on Terra's Agora forum. After gaining support and feedback from the community, a proposer drafts and submits a proposal alongside an initial deposit.
### Deposit period ###
After a proposal is submitted, it enters the deposit period, where it must reach a total minimum deposit of 512 Luna within 7 days from the time of its submission. The deposit threshold is reached when the sum of the initial deposit (from the proposer) and the deposits from all other interested network participants meet or exceed 512 Luna.Deposits protect against unnecessary proposals and spam.  
Deposits get refunded if all of the following conditions are met:
The minimum deposit of 512 Luna is reached within the 7-day deposit period,
Quorum is met: all casted votes represent more than 30% of all staked Luna, 
The total number of NoWithVeto votes is less than 33.4% of the total vote. A vote returns a majority of Yes or No votes.
### Votin Period & Options ###
If the minimum deposit has been reached before the end of the deposit period, then the proposal goes into a one-week voting period. While the proposal is in voting, holders of staked Luna can cast votes for the proposal.  
The 4 voting options available are:

* Yes: in favor.
* No: not in favor.
* NoWithVeto: not in favor, and the creator should lose their deposit.
* Abstain: neither for or against. An abstain vote counts toward meeting quorum but does not count toward the threshold.

Delegators vote using their staked Luna. One staked Luna equals one vote.If a delegator does not specify a vote with their staked Luna, their vote defaults to the vote cast by the validator their Luna is staked to. Delegators can override a validator's vote at any time during the voting period by voting with their staked Luna.


## Methodology ###
 As Terra 2.0 has expanded, we’ve seen a number of governance proposals come to light. Analyze the voting activity on the most recent 5 proposals. Can you identify any trends or patterns in voting?
Bonus: Dig up and compare the text of 2 governance proposals. What do you think of these proposals? What would have made them stronger or likelier to gather more votes? Do you have any improvements to recommend?  
To answer these questions 2 tables from Flipside Crypto Data Base were used:
 * terra.core.fact_governance_votes   
 * terra.core.fact_msg_attributes  
 finally two proposal text reviewed and commented, one recently passed propsal ["Control Protocol Grant Proposal"]() with ID3665

 """
         )


st.write("""   
##### Sources #####   """)
st.write("""    1.https://docs.terra.money/develop/module-specifications/spec-governance/  
        2.https://www.bloomberg.com/news/articles/2022-05-14    
        3.https://docs.terra.money/learn/station/governance/  
        4.https://docs.terra.money/develop/module-specifications/spec-governance/  

              """)


c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Project GuitHub:  [Governance Grind](https://github.com/Kaizen-Step/Governance_Grind)**', icon="💻")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Twitter:  [Luwig.1989](https://flipsidecrypto.xyz/)**', icon="🧠")
