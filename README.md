# mkdocs-audiotag

This is a plugin for the wonderful [mkdocs](https://www.mkdocs.org/) static site generator that allows for easy embedding of audio files using the default HTML5 audio element.

This plugin was made as an alternative to [mkdocs-audio](https://github.com/jfcmontmorency/mkdocs-audio), in order to support embedding multiple audio file sources. This is sometimes necessary because file formats and container types are not supported equally well in different browsers or on different platforms.

## Quick start

### Install the plugin

```shell
pip install mkdocs-audiotag
```

### Enable the plugin in mkdocs.yml

```yaml
plugins:
  - mkdocs-audiotag
```

### Embed an audio file

```markdown
![audio/ogg](my-audio-file.ogg)
```

Note: `audio/ogg` is the MIME type for the embedded file.

## Configuration

You can customize the behavior and appearance of the audio element by specifying options under the plugin in your `mkdocs.yml`. The defaults are sane, so in most cases this isn't necessary.

```yaml
# Default options
plugins:
  - mkdocs-audiotag:
      autoplay: false
      controls: true
      loop: false
      muted: false
      preload: 'metadata'
      width: 100%
```

### Options

- **autoplay**:
  If `true`, audio will start playing automatically when the page loads.
  [MDN: autoplay](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#autoplay)

- **controls**:
  If `true`, playback controls (play, pause, etc.) are shown.
  [MDN: controls](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#controls)

- **loop**:
  If `true`, audio will restart automatically after finishing.
  [MDN: loop](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#loop)

- **muted**:
  If `true`, audio will be muted on page load.
  [MDN: muted](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#muted)

- **preload**:
  Controls what gets downloaded on page load:
  - `'none'`: Don’t preload audio
  - `'metadata'`: Preload only metadata (default)
  - `'auto'`: Preload the whole file
  [MDN: preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#preload)

- **width**:  
  Sets the CSS width of the audio player (e.g., `'100%'`, `'300px'`).  
  [MDN: style](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#styling_with_css)

### Config examples

#### Use the default config options

```yaml
plugins:
  - mkdocs-audiotag
```

#### Set audio playback to loop, don't preload anything

```yaml
plugins:
  - mkdocs-audiotag:
      loop: true
      preload: none
```

#### Set the width of the audio player to 300 pixels

```yaml
plugins:
  - mkdocs-audiotag:
      width: 300px
```

## How to write the markdown content

There is no standard way to describe audio media in markdown. Inspired by [mkdocs-audio](https://github.com/jfcmontmorency/mkdocs-audio), we use the same syntax as with images. Instead of a title or a static marker, we specify the file's [MIME type](#mime-types), which **must begin with** `audio/` (otherwise, the plugin will not recognise the tag).

```markdown
![audio/ogg](my-audio-file.ogg)
```

To specify multiple source files, just include another file **immediately below the first line, i.e. with no extra line breaks**. The browser will try to load the first audio file. If that fails, it will move on to the next one, and so forth. This means you can put the preferred format first, and then add fallback options below. See [notes on this browser behavior at MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#usage_notes).

```markdown
![audio/ogg](my-audio-file.ogg)
![audio/mpeg](my-audio-file.mp3)
```

If you need to caption the audio element, use a separate plugin for that.

### MIME types

Some MIME types for common audio file formats are:

- AAC/M4A: audio/mp4
- MP3: audio/mpeg
- OGG: audio/ogg
- FLAC: audio/flac
- WAVE: audio/wav
- AIFF: audio/aiff
