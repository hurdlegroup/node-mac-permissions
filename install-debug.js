const os = require('os');
const {spawnSync} = require('child_process');

if (os.platform() === 'darwin') {
    spawnSync('npm', ['run', 'build-debug'], {
        input: 'darwin detected. Build native module.',
        stdio: 'inherit'
    });
}
