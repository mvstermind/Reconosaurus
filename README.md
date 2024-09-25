
# 🦖 Reconasaurus: The Ethical Dino of Doom 🦖

## Warning:
This README contains high levels of sarcasm, dino puns, and the slightest chance of being useful. If you're allergic to any of these, proceed with caution.

## What's This Thing?
Welcome to **Reconasaurus**, the *"ethical"* hacking tool that stomps around like a prehistoric beast, but with keyboards instead of claws. This glorious mess of a program helps you brute-force URLs, scan ports, and detect CMS platforms like a digital T-Rex with WiFi. It's perfect for wannabe hackers, real hackers, and, of course, velociraptors with an affinity for cybersecurity.

## Why? Just...Why?
Because dinosaurs are cool, and hacking is even cooler. Combine the two? You've got *Reconasaurus*. This tool is guaranteed to bring "Jurassic" level terror to unsuspecting servers (ethically, of course).

---

## Features (or "What Does This Thing Even Do?"):
- **🦕 Directory Brute-Forcing**: Why politely ask for web pages when you can just bash URLs with a wordlist and see what sticks?
- **🦖 Port Scanning**: Because if you don’t know which doors are open, how are you going to crash the party?
- **🐢 CMS Detection**: Sniff out WordPress, Joomla, and whatever ancient CMS systems are lurking in the web underworld.
- **💀 OS Detection**: *Guess what OS you're running?* Yep, our T-Rex can figure that out too. Who needs fingers when you have sharp teeth? (I mean...packets.)

---

## Installation (or How to Turn This Code Into a Working Tool):
### Requirements:
- **Python 3** 
- **Pip**

### Steps to Set Up the Dino Lair:
1. **Clone this repository** (because you don’t want to write this mess from scratch):
   ```bash
   git clone https://github.com/mvstermind/reconasaurus.git
   ```

2. **Install all the magical dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the beast**:
   ```bash
   python reconosaurus.py --type dir --url some-target.com
   ```

   Or, you know, pass in the arguments you actually want. Speaking of...

---

## Command-Line Arguments (a.k.a. Speak Dino to Me):
Here’s how you can talk to Reconasaurus without getting eaten:

### **Required Dino Commands**:
- `--url`: The web target you want to nom on. Must be in `http://` or `https://` format. If you forget, no recon for you.
  
- `--type`: What dino do you want to unleash? Options include:
  - `dir` - Brute-force directories like smashing rocks with a club.
  - `port` - Scan ports like you're knocking on someone's door, except noisier.
  - `cms` - Sniff out the CMS because even dinos love content management systems.

### **Optional Dino Snacks**:
- `--wordlist`: The list of words for your directory brute-force attack. Default is `./lists/dir-list.txt`, because defaults are boring but necessary.
  
- `--prefix`: Need to add some flair to your wordlist? Use this to slap on a prefix before smashing URLs. Perfect for those who want a little style with their chaos.

- `--scan`: Define the range of ports to scan (because, duh, you need a plan). Default is `1024`, but you can go wild with ranges like `80-443`. Reconasaurus approves.

- `--save`: Want to record the carnage? Use this option to save your results to a file. Nothing says "pro hacker" like logging everything to a `.txt`.

- `--os`: Find the operating system of your target. Reconasaurus is like Sherlock Holmes but...with claws.

---

## Example Usage (for when you just want to see how it works without reading):
```bash
python reconosaurus.py --url https://suspicioustarget.com --type dir --wordlist ./custom-list.txt --save report.txt
```
*Translation:* Reconasaurus is going to brute-force the heck out of `https://suspicioustarget.com`, using a custom wordlist, and save the carnage to `report.txt`.

```bash
python reconosaurus.py --url http://target.com --type port --scan 1-65535
```
*Translation:* Reconasaurus is knocking on every port on `http://target.com` from 1 to 65535. It's like trick-or-treating but much scarier.

```bash
python reconosaurus.py --url https://someblog.com --type cms
```
*Translation:* Our lovely beast is about to tell you which CMS this website is running—WordPress, Joomla, or something only dinosaurs remember.

---

## Fun Dino Facts (a.k.a. What to Expect):
- **Bugs**: No, not the kind you swat away. This tool might have actual coding bugs. Report them, or don't. It’s your life.
- **Output**: Colors! ASCII Art! Random status messages! This tool loves to make your terminal look like a retro arcade game.
- **Speed**: Fast enough to make you wonder if your internet is on fire. But hey, that’s what happens when you let a T-Rex loose on the web.

---

## License (Because Legal Stuff):
Reconasaurus is licensed under the MIT License, which basically means you can do whatever you want with it—*ethically*. If you use it for anything shady, that’s on you. Our T-Rex is not responsible for illegal activities, but he is excellent at eating lawyers.

---

## Final Thoughts:
If you made it this far, congrats—you’re either brave, bored, or lost. But hey, now you’ve got a cool new ethical hacking tool, some dino knowledge, and a questionable sense of humor. Go forth and hack responsibly (before Reconasaurus hacks back).
