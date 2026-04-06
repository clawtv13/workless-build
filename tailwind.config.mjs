/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Editorial Magazine palette (UI/UX Pro Max)
        primary: {
          DEFAULT: '#18181B',
          fg: '#FFFFFF',
        },
        secondary: {
          DEFAULT: '#3F3F46',
          fg: '#FFFFFF',
        },
        accent: {
          DEFAULT: '#EC4899',
          fg: '#FFFFFF',
          hover: '#DB2777',
        },
        background: '#FAFAFA',
        surface: {
          DEFAULT: '#FFFFFF',
          variant: '#E8ECF0',
        },
        text: {
          primary: '#09090B',      // Almost black - max contrast
          secondary: '#3F3F46',    // Dark gray - readable (was too light)
          tertiary: '#71717A',     // Medium gray - readable (was too light)
        },
        border: {
          DEFAULT: '#E4E4E7',
          light: '#F4F4F5',
        },
        error: {
          DEFAULT: '#DC2626',
          fg: '#FFFFFF',
        },
        // Legacy support (gradual migration)
        dark: '#18181B',
        darker: '#09090B',
      },
      fontFamily: {
        // Editorial typography (Cormorant Garamond + Libre Baskerville)
        heading: ['"Cormorant Garamond"', 'serif'],
        body: ['"Libre Baskerville"', 'serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
        // Legacy aliases
        display: ['"Cormorant Garamond"', 'serif'],
      },
      fontSize: {
        // Optimized type scale for readability
        'body': ['18px', { lineHeight: '1.75', letterSpacing: '0.01em' }],
        'body-sm': ['16px', { lineHeight: '1.6' }],
        'h1': ['48px', { lineHeight: '1.2', fontWeight: '600' }],
        'h2': ['36px', { lineHeight: '1.3', fontWeight: '600' }],
        'h3': ['24px', { lineHeight: '1.4', fontWeight: '600' }],
      },
      maxWidth: {
        'content': '1280px',
        'prose': '65ch', // 65-75 chars for readability
      },
      spacing: {
        // Consistent 4px/8px system
        '18': '4.5rem', // 72px
        '22': '5.5rem', // 88px
      },
    },
  },
  plugins: [],
}
