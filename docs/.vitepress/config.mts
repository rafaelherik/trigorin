import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Trigorin",
  description: "Useful custom policies to Checkov.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
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
      { icon: 'github', link: 'https://github.com/rafaelherik/trigorin' }
    ]
  }
})
