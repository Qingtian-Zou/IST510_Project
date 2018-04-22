#!/bin/bash

RELATIVE_SIZE=1.0
IMAGE_SIZE=224
ARCHITECTURE="mobilenet_${RELATIVE_SIZE}_${IMAGE_SIZE}"

strace -tt -e trace=execve,exit_group -o "${ARCHITECTURE}.strace" \
    python -m scripts.retrain \
        --bottleneck_dir=tf_files/"${ARCHITECTURE}"/bottlenecks \
        --model_dir=tf_files/models/ \
        --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
        --output_graph=tf_files/"retrained_${ARCHITECTURE}.pb" \
        --output_labels=tf_files/"labels_${ARCHITECTURE}.txt" \
        --architecture="${ARCHITECTURE}" \
        --image_dir=256_ObjectCategories
