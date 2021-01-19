# Unsplash Image Search

Search photos on Unsplash using natural language descriptions powered by OpenAI's [CLIP model](https://github.com/openai/CLIP).

There are two variants of the search:

-   [Searching photos in the Unsplash Dataset](#searching-photos-in-the-unsplash-dataset) - search for photos in the whole [Unsplash Dataset](https://github.com/unsplash/datasets) using CLIP.
-   [Searching on unsplash.com](#searching-photos-on-unsplashcom) - fetch 100 photos from [unsplash.com](https://unsplash.com) and select the best matches using CLIP.

## Setup

Follow the steps below to setup your environment.

1. Install the dependencies from the `requirements.txt`

```
pip install -r requirements.txt
```

2. Run the `setup-clip.ipynb` notebook to setup CLIP.

## Searching photos in the Unsplash Dataset

You will need to precompute the image features using CLIP for all photos in the [Unsplash Dataset](https://github.com/unsplash/datasets). I will soon share the precomputed files so you can jump directly into the search!

1. Run the `download-unsplash-dataset.ipynb` to download all photos.
2. Run the `process-unsplash-dataset.ipynb` to compute the feature vectors with CLIP.
3. Run the `search-image-dataset.ipynb` to seach for images with a natural language query.

### Examples

See more examples [on Twitter](https://twitter.com/haltakov/status/1351414975332495360).

#### Two dogs playing in the snow

![Result #1 for "Two dogs playing in the snow"](images/dog_1.jpg)

![Result #2 for "Two dogs playing in the snow"](images/dog_2.jpg)

![Result #3 for "Two dogs playing in the snow"](images/dog_3.jpg)

## Searching photos on unsplash.com

Use the `search-image.ipynb` notebook to fetch images from the Unsplash API and then find the best matches to a natural language query.

### Examples

#### A car driving in the woods

We want to find photos on Unsplash that are described by the phrase **a car driving in the woods**.

First, we fetch 100 images for the keyword `car` from the Unsplash API. They contain all kinds of photos of cars.

![Search results for "car" on Unsplash](images/car_woods_all.jpg)

Then, we use CLIP to find the photos that best match the phrase.

![Selected image #1 for "a car driving in the woods" using CLIP](images/car_woods_1.jpg)

Photo by [Jorgen Hendriksen](https://unsplash.com/@jor9en?utm_source=ml_image_search&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=ml_image_search&utm_medium=referral)

![Selected image #1 for "a car driving in the woods" using CLIP](images/car_woods_2.jpg)

Photo by [Matthew Ronder-Seid](https://unsplash.com/@matthewronderseid?utm_source=ml_image_search&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=ml_image_search&utm_medium=referral)

![Selected image #1 for "a car driving in the woods" using CLIP](images/car_woods_3.jpg)

Photo by [Michael Heuser](https://unsplash.com/@gum_meee?utm_source=ml_image_search&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=ml_image_search&utm_medium=referral)

## How It Works

[CLIP](https://openai.com/blog/clip/) is a new neural network model from OpenAI trained on huge ammount of images and text descriptions. The network can be used to transform both images and text in the same latent space. This means that we can then evaluate the similarities of images with text!

## Acknowledgement

This project was inspired by these projects:

-   [Beyond tags and entering the semantic search era on images with OpenAI CLIP](https://towardsdatascience.com/beyond-tags-and-entering-the-semantic-search-era-on-images-with-openai-clip-1f7d629a9978) by [Ramsri Goutham Golla](https://twitter.com/ramsri_goutham)
-   [Alph, The Sacred River](https://github.com/thoppe/alph-the-sacred-river) by [Travis Hoppe](https://twitter.com/metasemantic)
-   [OpenAI's CLIP](https://github.com/openai/CLIP)
-   [Unsplash](https://unsplash.com/)
