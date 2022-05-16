import { computed } from "vue";
import fs from "fs";
import pathModule from "path";

export function getFiles(path) {
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

  return {
    files,
  };
}
