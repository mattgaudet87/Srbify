// The one place that decides whether an entry is shown: vulgar entries stay hidden unless Settings turns them on.
export const isVisible = (e, { showVulgar }) => showVulgar || e.register !== 'vulgar'
