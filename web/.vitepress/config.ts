import { defineConfig } from "vitepress";

import graderItems from "./grader.g";
import examItems from "./exam.g";

export default defineConfig({
  lang: "th",
  title: "Shitcode Collection",
  description:
    "Website containing my solutions for Com Prog | เอาไว้โชว์เฉย ๆ ไม่ได้ให้ลอก",
  lastUpdated: true,
  outDir: "../dist",

  head: [
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=IBM+Plex+Sans+Thai:r,i,b,bi",
      },
    ],
  ],

  themeConfig: {
    footer: {
      message: "Released under the MIT License",
      copyright: "Copyright © 2022 Nutthapat Pongtanyavichai",
    },
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/Leomotors/2110101-com-prog",
      },
    ],

    sidebar: [
      {
        collapsible: true,
        text: "Introduction",
        items: [
          {
            text: "Hello World",
            link: "/introduction/",
          },
          {
            text: "เฉลยพร้อมคำอธิบาย",
            link: "https://com-pog.leomotors.net",
          },
        ],
      },
      {
        collapsible: true,
        collapsed: true,
        text: "Grader Solutions",
        items: graderItems,
      },
      {
        collapsible: true,
        collapsed: true,
        text: "Exam Solutions",
        items: examItems,
      },
    ],
  },
});
