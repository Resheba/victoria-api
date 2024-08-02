#!/bin/bash

uvicorn src.app.app:app --factory --reload --host 0.0.0.0 --port 80
