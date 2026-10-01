export const CATEGORIES = [
  { slug: 'greetings-and-goodbyes', image: '/images/cafe-street-sunset.jpg', name: 'Greetings and goodbyes', icon: 'chat', subcategories: ['Hello', 'Goodbye', 'Good morning and night', 'How are you', 'Answers to how are you', 'Manners (thanks, sorry, please)'] },
  { slug: 'texting-and-slang', focus: '30%', image: '/images/laptop-coffee-city.jpg', name: 'Texting and slang', icon: 'texting', subcategories: ['Reactions (ludilo, crkoh)', 'Laughing', 'Disbelief (ma daj)', 'Cool and lame', 'Texting abbreviations', 'Attitude words (bre, ajde, ma, joj)'] },
  { slug: 'swearing', focus: '55%', image: '/images/victor-monument-sunset.jpg', name: 'Swearing', icon: 'alert', subcategories: ['Mild (bre, majke mi)', 'Medium (jebote)', 'Strong', 'What each one really means', "When it's OK"] },
  { slug: 'flirting-and-romance', focus: '88%', image: '/images/couple-sunset.jpg', name: 'Flirting and romance', icon: 'heart', subcategories: ['Compliments', 'Missing you', 'Nicknames and pet names', 'Good night and good morning', 'Sweet sign-offs'] },
  { slug: 'teasing-and-comebacks', image: '/images/fortress-tree-sunset.jpg', name: 'Teasing and comebacks', icon: 'smile', subcategories: ['Denying (nisam to rekao)', 'Calling out teasing (zezaš me)', 'Comebacks', 'Playful insults', 'Owning it (nemoguć sam)'] },
  { slug: 'making-plans', image: '/images/coffee-water-notebook.jpg', name: 'Making plans', icon: 'calendar', subcategories: ['Inviting', 'When and where', 'Confirming (važi, može)', 'Running late', 'Cancelling and rescheduling'] },
  { slug: 'conversation-fillers', focus: '35%', image: '/images/street-lamp-river.jpg', name: 'Conversation fillers', icon: 'bubbles', subcategories: ['Agreeing (tačno, tako je)', 'Active listening (aha, jeste)', 'Reacting', 'Thinking words (pa, znači, ono)', 'Doubt (sumnjam, ne bih rekao)', 'Softeners (nema veze)'] },
  { slug: 'questions', image: '/images/church-dome.jpg', name: 'Questions', icon: 'help', subcategories: ['Question words (who, what, where...)', 'Which and what kind (koji, kakav)', "Common questions she'll ask", 'How to answer them'] },
  { slug: 'building-blocks', image: '/images/camera-map-fortress.jpg', name: 'Building blocks', icon: 'cube', subcategories: ['Pronouns', 'To be (sam, si, je)', 'Not (nisam, ne-)', 'My and your', 'Glue words (and, but, also, baš)', 'Numbers'] },
  { slug: 'verbs', image: '/images/train-platform-backpack.jpg', name: 'Verbs', icon: 'bolt', subcategories: ['Everyday verbs (present)', 'Past tense', 'Future (zvaću)', 'Commands (dođi, spavaj)', 'Can, want, have to'] },
  { slug: 'describing-words', image: '/images/backpack-map-bridge.jpg', name: 'Describing words', icon: 'sparkle', subcategories: ['Feelings (tired, happy, hungry)', 'People (cute, crazy, funny)', 'Things (good, sick, boring)', 'Opposites with ne-'] },
  { slug: 'things-and-places', focus: '60%', image: '/images/sign-putovanja-map.jpg', name: 'Things and places', icon: 'pin', subcategories: ['Food and drink', 'Going out', 'Home', 'Places', 'People and family', 'Time and days', 'Events (svadba, slava)'] },
  { slug: 'meeting-family-and-friends', focus: '80%', image: '/images/friends-picnic-sunset.jpg', name: 'Meeting family and friends', icon: 'users', subcategories: ['Polite greetings', 'Being a good guest', 'Compliments to the cook', 'Toasts (živeli)', 'Small talk'] },
  { slug: 'culture', image: '/images/cevapi-table.jpg', name: 'Culture', icon: 'landmark', subcategories: ['Holidays and traditions', 'Table manners and toasting', 'Common sayings and idioms', 'Things not to say'] },
]

export const bySlug = (slug) => CATEGORIES.find((c) => c.slug === slug)
export const byName = (name) => CATEGORIES.find((c) => c.name === name)
