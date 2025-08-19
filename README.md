# Stretching Timer

Minimal, configurable stretching timer with automatic progression and mobile-friendly design.

## Features

- **Single-file deployment** - Each timer is a self-contained HTML file
- **Automatic progression** - Moves through exercises and reps automatically
- **Clickable exercise list** - Jump to any exercise by clicking it
- **Mobile responsive** - Works on all devices
- **Exercise images** - Optional images for each exercise
- **Real-time countdown** - Shows current and total remaining time

## Quick Start

1. **Configure exercises** in `configs/[name].json`
2. **Deploy** with `python3 deploy.py` - pure python
3. **Open** `_release/[name]/index.html` in browser

## Configuration

Create JSON files in `configs/` directory:

```json
{
  "name": "Neck Stretching",
  "exercises": [
    {
      "name": "Chin Back",
      "duration": 5,
      "reps": 25,
      "image": "chin-back.png"
    },
    {
      "name": "Break",
      "duration": 10,
      "reps": 1,
      "isBreak": true
    }
  ]
}
```

## Images

Place exercise images in `images/[config-name]/` directory. Images are optional and referenced by filename in the config.

## Deployment

```bash
python deploy.py
```

Generates static HTML files in `_release/` directory. Each subdirectory contains a complete, deployable timer.
