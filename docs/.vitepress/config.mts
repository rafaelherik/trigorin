import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Suvorin",
  description: "Useful custom policies to Checkov.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: { light: 'logo-black.png', dark: 'logo-white.png' },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/usage-examples' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Usage examples', link: '/usage-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/rafaelherik/suvorin' }
    ]
  }
})
