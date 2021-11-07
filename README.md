<div align = "center">

<h1><a href="https://2kabhishek.github.io/SYN-detector">SYN-detector</a></h1>

<a href="https://github.com/2KAbhishek/SYN-detector/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/SYN-detector?style=plastic&color=white&label=License"> </a>

<a href="https://github.com/2KAbhishek/SYN-detector/pulse">
<img alt="Updated" src="https://img.shields.io/github/last-commit/2kabhishek/SYN-detector?style=plastic&color=e30724&label=Updated"> </a>

<a href="https://github.com/2KAbhishek/SYN-detector/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/SYN-detector?style=plastic&color=00d451&label=Stars"></a>

<a href="https://github.com/2KAbhishek/SYN-detector/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/SYN-detector?style=plastic&color=1688f0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/SYN-detector/watchers">
<img alt="Watchers" src="https://img.shields.io/github/watchers/2kabhishek/SYN-detector?style=plastic&color=ff5500&label=Watchers"> </a>

<a href="https://github.com/2KAbhishek/SYN-detector/graphs/contributors">
<img alt="Contributors" src="https://img.shields.io/github/contributors/2kabhishek/SYN-detector?style=plastic&color=f0f&label=Contributors"> </a>

<a href="https://github.com/2KAbhishek?tab=followers">
<img alt="Followers" src="https://img.shields.io/github/followers/2kabhishek?color=222&style=plastic&label=Followers"> </a>

<h3>Analyzes network to detect possible SYN scans 🕵️🔎</h3>

<figure>
  <img src= "https://raw.githubusercontent.com/2KAbhishek/SYN-detector/main/images/screenshot.png" alt="SYN-detector Demo" style="width:100%">
  <br/>
  <figcaption>SYN-detector screenshot</figcaption>
</figure>

</div>

## What is this

SYN-detector is a tool that analyzes a PCAP file in order to detect possible SYN scans.

## Inspiration

Was reading up on newtwork security and found about a technique called SYN scan and learned these:

- Used to find open ports for attack
- Scanenr sends out TCP SYN packets (the first packet in the TCP handshake) and watches for hosts that respond with SYN+ACK packets (the second handshake step)
- Number of SYN packets is much higher than the number of SYN+ACK packets

Wanted to build a tool to detect possible SYN scans.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of `python, scapy`

## Getting SYN-detector

To install SYN-detector, follow these steps:

```bash
git clone https://github.com/2kabhishek/SYN-detector
cd SYN-detector
```

## Using SYN-detector

You'll need to have a PCAP file to analyze.

I have a PCAP file `test-data.pcap` that I used to test SYN-detector.

```bash
USAGE:
    python syn-detector.py ./test-data.pcap

```

## How it was built

SYN-detector was built using `scapy`

## Challenges faced

While building SYN-detector the main challenges were:

- Figuring out TCP flags

## What I learned

- Learned a lot about network security
- Hands on with scapy

## What's next

Will make few more scripts using `scapy`.

Hit the ⭐ button if you found this useful.

## More Info

<div align="center">

<a href="https://github.com/2KAbhishek/SYN-detector">Source</a> |
<a href="https://2kabhishek.github.io/SYN-detector">Website</a>

</div>
