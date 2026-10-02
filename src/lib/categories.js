// Organized around "what am I trying to say right now?". Each subcategory is an intent
// (e.g. "Agree and disagree"); an entry can live in several of them (see `placements` in entries.json).
// Verbs and actions + Basics are the grammar-style sections.
export const CATEGORIES = [
  { slug: 'quick-phrases', image: '/images/cafe-street-sunset.jpg', name: 'Quick phrases', icon: 'bubbles', blurb: 'The common words you use all day',
    subcategories: ['Greetings and goodbyes', 'Conversation starters', 'Yes, no, maybe', 'Thanks, sorry, please', 'Agree and disagree', 'Reactions', 'Common replies', 'Filler and transition words'] },
  { slug: 'conversation', image: '/images/friends-picnic-sunset.jpg', name: 'Conversation', icon: 'chat', blurb: 'Asking, answering, making plans',
    subcategories: ['Introductions', 'Questions', 'Answering questions', 'Getting to know someone', 'Making plans', 'Confirming plans', 'Running late', 'Cancelling', 'Casual conversation', 'Teasing and comebacks', 'Formal and polite'] },
  { slug: 'flirting-and-relationships', focus: '88%', image: '/images/couple-sunset.jpg', name: 'Flirting and relationships', icon: 'heart', blurb: 'Compliments, dates, pet names',
    subcategories: ['Compliments', 'Flirting', 'I like you', 'Missing someone', 'Affection and romance', 'Good morning and good night', 'Nicknames and pet names', 'Playful teasing', 'Dating', 'Relationship talk'] },
  { slug: 'describing-and-feelings', image: '/images/backpack-map-bridge.jpg', name: 'Describing and feelings', icon: 'sparkle', blurb: 'Feelings, people, things, opinions',
    subcategories: ['Emotions', 'Physical states', 'People: personality', 'People: appearance', 'Describing things', 'Opinions', 'Comparisons', 'Opposites'] },
  { slug: 'everyday-situations', focus: '60%', image: '/images/sign-putovanja-map.jpg', name: 'Everyday situations', icon: 'pin', blurb: 'At a café, shopping, getting around',
    subcategories: ['Food and drink', 'Restaurants and cafés', 'Going out', 'Home', 'Shopping and money', 'Places', 'Directions', 'Travel and transportation', 'Friends and family', 'Events', 'Holidays and celebrations'] },
  { slug: 'verbs-and-actions', image: '/images/train-platform-backpack.jpg', name: 'Verbs and actions', icon: 'bolt', blurb: 'Grammar: verbs, tenses, commands', grammar: true,
    subcategories: ['Everyday verbs', 'Can and can’t', 'Want and don’t want', 'Need and have to', 'Present', 'Past', 'Future', 'Commands', 'Requests', 'Invitations'] },
  { slug: 'basics', image: '/images/camera-map-fortress.jpg', name: 'Basics', icon: 'cube', blurb: 'Grammar: pronouns, numbers, glue words', grammar: true,
    subcategories: ['Pronouns', 'My, your, his, her', 'This and that', 'Numbers', 'Time and days', 'Colors', 'Shapes and sizes', 'Question words', 'And, but, because', 'Prepositions', 'Flow words'] },
  { slug: 'slang-and-swearing', focus: '55%', image: '/images/victor-monument-sunset.jpg', name: 'Slang and swearing', icon: 'alert', blurb: 'Texting slang, attitude, tone warnings',
    subcategories: ['Texting slang', 'Abbreviations', 'Attitude words', 'Reactions', 'Casual slang', 'Mild swearing', 'Strong swearing', 'Insults', 'Playful insults', 'Tone and usage warnings'] },
  { slug: 'culture-and-etiquette', image: '/images/cevapi-table.jpg', name: 'Culture and etiquette', icon: 'landmark', blurb: 'Family, guests, toasts, sayings',
    subcategories: ['Meeting family', 'Talking to elders', 'Being a guest', 'Toasts', 'Holidays', 'Common sayings', 'Idioms', 'Things not to say', 'Cultural context'] },
]

export const bySlug = (slug) => CATEGORIES.find((c) => c.slug === slug)
export const byName = (name) => CATEGORIES.find((c) => c.name === name)

// An entry can sit in several categories. `placements` is the full list; category/subcategory is the primary one.
export const placementsOf = (entry) => entry.placements?.length ? entry.placements : [{ category: entry.category, subcategory: entry.subcategory }]
export const inCategory = (entry, catName) => placementsOf(entry).some((p) => p.category === catName)
