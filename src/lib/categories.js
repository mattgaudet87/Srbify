export const CATEGORIES = [
  { slug: 'greetings-and-goodbyes', name: 'Greetings and goodbyes', icon: '👋', subcategories: ['Hello', 'Goodbye', 'Good morning and night', 'How are you', 'Answers to how are you', 'Manners (thanks, sorry, please)'] },
  { slug: 'texting-and-slang', name: 'Texting and slang', icon: '💬', subcategories: ['Reactions (ludilo, crkoh)', 'Laughing', 'Disbelief (ma daj)', 'Cool and lame', 'Texting abbreviations', 'Attitude words (bre, ajde, ma, joj)'] },
  { slug: 'swearing', name: 'Swearing', icon: '🤬', subcategories: ['Mild (bre, majke mi)', 'Medium (jebote)', 'Strong', 'What each one really means', "When it's OK"] },
  { slug: 'flirting-and-romance', name: 'Flirting and romance', icon: '💘', subcategories: ['Compliments', 'Missing you', 'Nicknames and pet names', 'Good night and good morning', 'Sweet sign-offs'] },
  { slug: 'teasing-and-comebacks', name: 'Teasing and comebacks', icon: '😏', subcategories: ['Denying (nisam to rekao)', 'Calling out teasing (zezaš me)', 'Comebacks', 'Playful insults', 'Owning it (nemoguć sam)'] },
  { slug: 'making-plans', name: 'Making plans', icon: '📅', subcategories: ['Inviting', 'When and where', 'Confirming (važi, može)', 'Running late', 'Cancelling and rescheduling'] },
  { slug: 'conversation-fillers', name: 'Conversation fillers', icon: '🗨️', subcategories: ['Agreeing (tačno, tako je)', 'Active listening (aha, jeste)', 'Reacting', 'Thinking words (pa, znači, ono)', 'Doubt (sumnjam, ne bih rekao)', 'Softeners (nema veze)'] },
  { slug: 'questions', name: 'Questions', icon: '❓', subcategories: ['Question words (who, what, where...)', 'Which and what kind (koji, kakav)', "Common questions she'll ask", 'How to answer them'] },
  { slug: 'building-blocks', name: 'Building blocks', icon: '🧱', subcategories: ['Pronouns', 'To be (sam, si, je)', 'Not (nisam, ne-)', 'My and your', 'Glue words (and, but, also, baš)', 'Numbers'] },
  { slug: 'verbs', name: 'Verbs', icon: '🏃', subcategories: ['Everyday verbs (present)', 'Past tense', 'Future (zvaću)', 'Commands (dođi, spavaj)', 'Can, want, have to'] },
  { slug: 'describing-words', name: 'Describing words', icon: '🎨', subcategories: ['Feelings (tired, happy, hungry)', 'People (cute, crazy, funny)', 'Things (good, sick, boring)', 'Opposites with ne-'] },
  { slug: 'things-and-places', name: 'Things and places', icon: '🏠', subcategories: ['Food and drink', 'Going out', 'Home', 'Places', 'People and family', 'Time and days', 'Events (svadba, slava)'] },
  { slug: 'meeting-family-and-friends', name: 'Meeting family and friends', icon: '👨‍👩‍👧', subcategories: ['Polite greetings', 'Being a good guest', 'Compliments to the cook', 'Toasts (živeli)', 'Small talk'] },
  { slug: 'culture', name: 'Culture', icon: '🏛️', subcategories: ['Holidays and traditions', 'Table manners and toasting', 'Common sayings and idioms', 'Things not to say'] },
]

export const bySlug = (slug) => CATEGORIES.find((c) => c.slug === slug)
export const byName = (name) => CATEGORIES.find((c) => c.name === name)
