<div align = "center">

<h1><a href="https://2kabhishek.github.io/syn-detector">syn-detector</a></h1>

<a href="https://github.com/2KAbhishek/syn-detector/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/syn-detector?style=plastic&color=white&label=License"> </a>

<a href="https://github.com/2KAbhishek/syn-detector/pulse">
<img alt="Updated" src="https://img.shields.io/github/last-commit/2kabhishek/syn-detector?style=plastic&color=e30724&label=Updated"> </a>

<a href="https://github.com/2KAbhishek/syn-detector/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/syn-detector?style=plastic&color=00d451&label=Stars"></a>

<a href="https://github.com/2KAbhishek/syn-detector/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/syn-detector?style=plastic&color=1688f0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/syn-detector/watchers">
<img alt="Watchers" src="https://img.shields.io/github/watchers/2kabhishek/syn-detector?style=plastic&color=ff5500&label=Watchers"> </a>

<a href="https://github.com/2KAbhishek/syn-detector/graphs/contributors">
<img alt="Contributors" src="https://img.shields.io/github/contributors/2kabhishek/syn-detector?style=plastic&color=f0f&label=Contributors"> </a>

<a href="https://github.com/2KAbhishek?tab=followers">
<img alt="Followers" src="https://img.shields.io/github/followers/2kabhishek?color=222&style=plastic&label=Followers"> </a>

<h3>Analyzes network to detect possible syn scans 🕵️🔎</h3>

<figure>
  <img src= "https://raw.githubusercontent.com/2KAbhishek/syn-detector/main/images/screenshot.png" alt="syn-detector Demo" style="width:100%">
  <br/>
  <figcaption>syn-detector screenshot</figcaption>
</figure>

</div>

## What is this

syn-detector is a tool that analyzes a PCAP file in order to detect possible syn scans.

## Inspiration

Was reading up on network security and found about a technique called SYN scan and learned these:

- Used to find open ports for attack
- Scanner sends out TCP SYN packets (the first packet in the TCP handshake) and watches for hosts that respond with SYN+ACK packets (the second handshake step)
- Number of SYN packets is much higher than the number of SYN+ACK packets

Wanted to build a tool to detect possible SYN scans.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of `python, scapy`

## Getting syn-detector

To install syn-detector, follow these steps:

```bash
git clone https://github.com/2kabhishek/syn-detector
cd syn-detector
```

## Using syn-detector

You'll need to have a PCAP file to analyze.

I have a PCAP file `test-data.pcap` that I used to test SYN-detector.

```bash
USAGE:
    python syn-detector.py ./test-data.pcap

```

## How it was built

syn-detector was built using `scapy`

## Challenges faced

While building syn-detector the main challenges were:

- Figuring out TCP flags

## What I learned

- Learned a lot about network security
- Hands on with scapy

## What's next

Will make few more scripts using `scapy`.

Hit the ⭐ button if you found this useful.

## More Info

<div align="center">

<a href="https://github.com/2KAbhishek/syn-detector">Source</a> |
<a href="https://2kabhishek.github.io/syn-detector">Website</a>

</div>
