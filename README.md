# RM.pad
A mechanical macropad designed for productivity and musical expression with a minimalistic and clean design.

## Features
* Three Layers: Productivity, System/Media, and a bonus mini MIDI Instrument.
* Layer-Specific Lighting: Visual feedback that changes depening on which layer you are currently using.
* Multi-Function Rotary Encoder: Context-aware knob for volume, scrolling, and MIDI CC.
  
<img width="852" height="613" alt="image" src="https://github.com/user-attachments/assets/0f059985-2d6f-4049-89e5-64a161b8bef6" />
<img width="1281" height="803" alt="image" src="https://github.com/user-attachments/assets/b061507d-ae78-4865-afca-f10018d173da" />
<img width="1053" height="705" alt="image" src="https://github.com/user-attachments/assets/356652c0-4e0f-44dc-a00c-0b6338c0e8d0" />

## Usage

The RM.pad uses a layer system. Navigation and feedback are handled via the bottom-left key and the integrated NeoPixels.

### Layer Navigation
* **Switching Layers:** Press the bottom-left key to cycle through modes!
* **Visual Indicators:**
    * Deep Blue: Layer 0 (Productivity focused)
    * Sky Blue: Layer 1 (System focused)
    * White: Layer 2 (MIDI)

### Layer 0: Productivity (Deep Blue)
Designed for Windows OS and browser navigation.
* **Top Row:** Open Run Command (Win+R), New Tab (Ctrl+T), Focus Address Bar (Ctrl+L).
* **Middle Row:** Show Desktop (Win+D), Close Window (Alt+F4), Maximize Window (Win+Up).
* **Bottom Row:** Cycle Layer, Text Macro (Pre-defined sentence), Lock PC (Win+L).
* **Encoder:** Rotate for Volume Up/Down; Press to Mute.

### Layer 1: System and Media (Sky Blue)
Designed for media playback and hardware settings.
* **Top Row:** Play/Pause, Next Track, Previous Track.
* **Middle Row:** Toggle RGB Power, Cycle RGB Animations, Reset to Static Sky Blue.
* **Bottom Row:** Cycle Layer, No Command (for now), Reset Microcontroller.
* **Encoder:** Rotate for Page Up/Down; Press for Home key.

### Layer 2: MIDI Keyboard (White)
Turns the macropad into a musical instrument for DAWs or web synths.
* **Keypad:** 8 keys mapped to the C-Major scale (C, D, E, F, G, A, B, C).
* **Bottom-Left Key:** Cycles back to Layer 0.
* **Encoder:** Rotate to send MIDI CC (Continuous Controller) data for like volume or filter cutoff.

### MIDI Integration
To use the MIDI layer, simply open your Digital Audio Workstation (DAW) and select "KMK MIDI" as the active MIDI Input device.

# Bill Of Materials

XIAO RP2040 Microcontroller - [here](https://www.amazon.in/Microcontroller-Dual-Core-MicroPython-CircuitPython-Interfaces/dp/B09NNVNW7M/ref=sr_1_1_sspa?nsdOptOutParam=true&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) (x1)

1N4148 / Diodes - [here](https://www.digikey.com/en/products/detail/onsemi/1N4148/458603) (x9)

Cherry MX Keys - [here](https://www.amazon.in/dp/B09ZT8BY6W/ref=twister_B0BFGC2MJY?_encoding=UTF8) (x9)

SK6812 Mini - [here](https://keeb.io/products/sk-6812-mini-e-rgb-leds-12-pack) (x3)

EC11 Rotary Encoder - [here](https://keeb.io/products/rotary-encoder-ec11) (x1)

1.7mm(diameter)x10mm screws (x4)  - [here](https://www.moddiy.com/products/M1.7-x-10mm-Black-Screws-(PM1.7X10).html)

Blank DSA Keycaps (Black)(x9) - [here](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/)


AI was used to polish `readme.md`
