# POWERLINE SWISSARMYKNIFE

A [Powerline](https://powerline.readthedocs.io/en/master/) segment. This segment shows the execution of complex command line defined by user.

By [Miguel de Dios Matias](https://github.com/mdtrooper).

## Installation

### Using pip

```
pip install powerline-swissarmyknife
```

## Configuration

You can activate the Powerline Slotmachine segment by adding it to your segment configuration,
for example in `.config/powerline/themes/shell/default.json`:

```json
{
    "function": "powerline_swissarmyknife.execute",
    "priority": 30,
    "args": {
        "commandLine": "ps aux --no-headers | wc -l",
        "postContent": "⚙️"
    }
},
```

Show the number of processes running in your system.

![screenshot number processes](https://raw.githubusercontent.com/mdtrooper/powerline_swissarmyknife/master/powerline_swissarmyknife_number_processes.jpg "screenshot number processes")

### Arguments
* **commandLine (string)**: The command line to execute, it can be complex (with pipes) (remember python3 runs as /bin/sh, not bash).
* **line (string)**: The string to format the content of segment.
  * Default: "{preContent}{output}{err}{postContent}"
* **preContent (string)**: The string to show before the result.
  * Default: ""
* **postContent (string)**: The string to show after the result.
  * Default: "🤖"
* **successCodes (list(int) or None)**: The values are success code return (normally 0), the background change to critical success.
  * Default: None
* **failureCodes (list(int) or None)**: The values are fail code return, the background change to critical failture. 
  * Default: None

### Examples

Shows the upload and download rate and count of torrents download in Deluge.

```json
{
    "function": "powerline_swissarmyknife.execute",
    "priority": 30,
    "args": {
        "commandLine": "deluge-console status | awk '/Total upload:/{print $3$4} /Total download:/{print $3$4} /Downloading:/{print $2\"D\"}' | tr '\n' ' '",
        "postContent": "️"
    }
},
```


![screenshot deluge](https://raw.githubusercontent.com/mdtrooper/powerline_dice/master/powerline_deluge.jpg "screenshot deluge")

Show a random pornstar from redtube api.

```json
{
    "function": "powerline_swissarmyknife.execute",
    "priority": 30,
    "args": {
        "commandLine": "if [ -f /tmp/list.redtube.json ]; then list=$(cat /tmp/list.redtube.json); else list=$(curl 'https://api.redtube.com/?data=redtube.Stars.getStarList&output=json'); echo $list > /tmp/list.redtube.json; fi; list_length=$(echo $list | jq '.stars | length'); rand=$(echo 'ibase=16;' $(openssl rand -hex 4 | tr '[a-z]' '[A-Z]')  | bc); echo $list | jq \".stars[$(echo \\\"$rand % $list_length\\\" | bc)].star.star_name\" -r",
        "postContent": " 🎥"
    }
},
```

![screenshot pornstar](https://raw.githubusercontent.com/mdtrooper/powerline_dice/master/powerline_pornstar.jpg "screenshot pornstar")

## License

Licensed under [the GPL3 License](https://github.com/mdtrooper/powerline_slotmachine/blob/master/LICENSE).