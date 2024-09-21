# Cloud Server Management Scripts

This repository is a collection of scripts designed for efficiently managing a NAS WD-CloudExtra server. These will facilitate various administrative tasks, making it easier to automate and streamline operations mostly on media files (audio, video, photos)

## Features on Audiofile

- **Sorting**: Cronjob running every midnight will check if the audio collection is properly sorted.
- **Deduplication**: A job will delete all files that are duplicated (based on hash value of the file).
- **File normalization**: A set of CLI commands will trigger jobs that normalizes all the names based on a pattern.
- **Automatic download**: Download audio files that were scrapped from soma.fm playlist.
- 

## Features on Video files
- **Deduplication**: A job for deduplication will delete all files that are duplicated (based on hash value of the file).
- **Shrinking vide size**: Job for shrinking video size so that it does not occupy so much space.
- **File normalization**: A set of CLI commands will trigger jobs that normalizes all the names based on a pattern (no clue how to do it actually).


## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:ExperimentalHypothesis/manage-scripts-for-nas-.git 
   cd 
   poetry install & poetry shell