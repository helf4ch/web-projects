import { ref, computed } from "vue";
import { app } from "@electron/remote";
import fs from "fs";
import pathModule from "path";

export function getFilesAndTracks() {
  const path = ref(app.getPath("music"));

  const files = computed(() => {
    const fileNames = fs.readdirSync(path.value);
    return fileNames
      .filter((file) => {
        const stats = fs.statSync(pathModule.join(path.value, file));
        if (pathModule.extname(file) === ".mp3" || stats.isDirectory()) {
          return true;
        }
        return false;
      })
      .map((file) => {
        const stats = fs.statSync(pathModule.join(path.value, file));
        return {
          name: file,
          path: pathModule.join(path.value, file),
          isDirectory: stats.isDirectory(),
        };
      })
      .sort((a, b) => {
        if (a.isDirectory === b.isDirectory) {
          return a.name.localeCompare(b.name);
        }
        return a.isDirectory ? -1 : 1;
      });
  });

  const trackList = computed(() => {
    return files.value
      .filter((file) => {
        if (!file.isDirectory) {
          return true;
        }
        return false;
      })
      .map((file) => {
        // 01: Artist - Title
        // only one : or -
        let parseName = [pathModule.parse(file.name).name];
        if (file.name.indexOf(":") + 1) {
          parseName = parseName[0].split(/\s*:\s*/);
          parseName.splice(0, 1);
        }
        if (file.name.indexOf("-") + 1) {
          parseName = parseName[0].split(/\s*-\s*/);
        }
        const artist = parseName[0];
        const title = parseName[1];
        return {
          artist: artist,
          title: title,
          path: file.path,
        };
      });
  });

  return {
    path,
    files,
    trackList,
  };
}
