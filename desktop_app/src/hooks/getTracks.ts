import { computed } from "vue";
import pathModule from "path";

export function getTracks(files) {
  const tracks = computed(() => {
    const value = files.value
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

    if (value.length === 0) {
      value.push({
        artist: "No tracks found",
        title: "Empty playlist",
        path: "",
      });
    }

    return value;
  });

  return {
    tracks,
  };
}
