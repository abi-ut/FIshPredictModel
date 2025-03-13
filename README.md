# Fish Species Prediction Model

## Overview

This project implements a **Logistic Regression** model to predict fish species based on various physical features of the fish. The model takes six input features—`Weight`, `Length1`, `Length2`, `Length3`, `Height`, and `Width`—and classifies the fish into one of the several species present in the dataset. This is a **multi-class classification** problem where the target variable is the species of the fish.

## Model Details

The **Logistic Regression** model used in this project is configured as follows:

- **Model Type**: Multinomial Logistic Regression
- **Solver**: `lbfgs` (a robust optimizer well-suited for smaller datasets)
- **Max Iterations**: 500 (to ensure convergence of the algorithm)
- **Random State**: 42 (ensures reproducibility of results)

### Hyperparameters
- **multi_class='multinomial'**: This setting allows the model to handle multiple classes (fish species) independently by using a multinomial logistic regression approach.
- **solver='lbfgs'**: The Limited-memory Broyden–Fletcher–Goldfarb–Shanno (LBFGS) algorithm is an optimization technique that works well for small datasets and multi-class classification problems.
- **max_iter=500**: The number of iterations for the solver, which helps ensure convergence and avoids issues in cases where the solution requires many iterations.
- **random_state=42**: The random seed used to initialize the random number generator, ensuring the results are reproducible.

## Purpose

The goal of the model is to classify a fish into one of several species based on its physical features. By using six different measurements, the model is able to make accurate predictions regarding the species of a fish, which could be useful in various fields, such as environmental studies, fisheries management, and biodiversity research.

### Model Performance

The performance of the model can be evaluated by metrics such as accuracy, precision, recall, and F1 score. These metrics assess how well the model classifies the fish species based on the input features.

## Dataset Information

The dataset used to train the model contains several attributes related to fish measurements:

- **Weight**: The weight of the fish in grams
- **Length1**: The length of the fish along one axis
- **Length2**: The length of the fish along another axis
- **Length3**: The length of the fish along the third axis
- **Height**: The height of the fish
- **Width**: The width of the fish

The target variable is the **Species** of the fish, which is one of several categories.

## Model Usage

The model can be used in various applications where classification of fish species is required based on their physical features. It can be integrated into a web interface (built using Flask), allowing users to enter the physical attributes of a fish and get a prediction of its species.

## Limitations and Future Work

- **Dataset Size**: The accuracy of the model may improve with a larger, more diverse dataset.
- **Feature Engineering**: Additional features such as water temperature or habitat could potentially improve model performance.
- **Model Refinement**: Future work could explore using more advanced models, such as decision trees or neural networks, for potentially better accuracy.

---


