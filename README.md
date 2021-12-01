# RC3: Razer Chroma Covert Channel
**RGB Keyboard Covert Channel Implementation**

*Brendan McGlynn, Ian Stroszeck, Wyatt Tauber*

## Abstract:

Covert channels exist best in benign environments, where information can be secretly passed from one person to another without raising suspicion. With the ubiquity of RGB peripherals in everyday life, especially among gamers, RGB keyboards make an excellent medium for hiding a covert channel in -- among all of the flashing, colored lights. This paper presents a Razer Chroma Covert Channel (RC3), a covert channel that uses the individual LEDs under each key to transmit and read encoded information, which we then scored using an evaluation framework consisting of transition methods (how to receive the data), bandwidth, accuracy, ease-of-use, and covertness. From our testing, we determined that using the ChromaEffects profile resulted in the largest bandwidth, as each key could hold up to 3 distinct ASCII values (one for each color), while also remaining easy to use, 100\% accurate, and relatively undetectable. The other implementations tested varied in these categories.

## Presentations:

[10/4/2021 Initial Idea Presentation](https://docs.google.com/presentation/d/1ubBkI0SmQaPemvky5MYLoTU6EjmY03P7WYBV3YcpTIg/edit?usp=sharing)

[10/20/2021 Progress Update Presentation](https://docs.google.com/presentation/d/1xvYmN7fN6vC1pj39nVuiw1uiE4QxeTgY0xgGsTU9DkI/edit?usp=sharing)

[11/08/2021 Demo Presentation](https://docs.google.com/presentation/d/1FGauN4EQoT6zvseTLbWzmSN0goxm-Ab_IeFHTqF6Zp8/edit?usp=sharing)

[11/17/2021 Venue Presentation](https://docs.google.com/presentation/d/1ZDV7YKsPH-JGDdBGoBPdmB7Uhcm8rM1nPqrbN8dl610/edit?usp=sharing)

[12/1/2021 Final Presentation](https://docs.google.com/presentation/d/1OmoCHqMvZjOzoyObxk5X6gf6WpRhL1m_t9W6NUwXFro/edit?usp=sharing)

## Usage:
./processing.py <ChromaEffects file>
