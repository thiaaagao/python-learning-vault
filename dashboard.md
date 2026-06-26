---
banner: Python Journey
---

# 🧭 Python Journey Dashboard

```dataviewjs
const progress = dv.page("data/progress");
const xpPage = dv.page("data/xp");
const flashcardsPage = dv.page("data/flashcards");

if (!progress || !xpPage) {
    dv.paragraph("⚠️ Dados de progresso ainda não carregados. Abra os arquivos em `data/` primeiro.");
} else {

const p = progress.progress;
const xp = xpPage.xp;

// --- STATUS CARD ---
dv.paragraph(`## 📊 Status Atual
**Level:** ${xp.level} | **XP:** ${xp.current}/${xp.level_thresholds[`level_${xp.level + 1}`] || "∞"}
**Streak:** ${p.study_streak} dias | **Fase Atual:** ${p.current_phase}
**Fases Completas:** ${p.phases_completed}/6`);

// --- XP BAR ---
const currentLevel = xp.level;
const currentXP = xp.current;
const threshold = xp.level_thresholds[`level_${currentLevel}`];
const nextThreshold = xp.level_thresholds[`level_${currentLevel + 1}`];
const progressXP = nextThreshold ? ((currentXP - threshold) / (nextThreshold - threshold) * 100) : 100;
dv.paragraph(`**XP para próximo level:** ${Math.round(progressXP)}%`);
const xpBar = `<progress value="${Math.round(progressXP)}" max="100" style="width:100%;height:18px;border-radius:8px;"></progress>`;
dv.span(xpBar);

// --- PHASES ---
dv.paragraph("## 📚 Progresso por Fase");
const fases = {1: "Fundamentos", 2: "Scripts", 3: "Ferramentas", 4: "Web & API", 5: "Dados", 6: "Projeto Final"};
for (let i = 1; i <= 6; i++) {
    const phase = p.phase_status[`phase_${i}`];
    const statusIcon = phase.status === "completed" ? "✅" : phase.status === "studying" ? "📖" : "⬜";
    dv.paragraph(`${statusIcon} **Fase ${i}:** ${fases[i]} — ${phase.progress_percent}%`);
    const bar = `<progress value="${phase.progress_percent}" max="100" style="width:100%;height:14px;border-radius:6px;"></progress>`;
    dv.span(bar);
}

// --- BADGES ---
dv.paragraph("## 🏅 Badges");
const badges = xp.badges;
if (badges.length === 0) {
    dv.paragraph("*Nenhuma badge conquistada ainda. Complete as fases para ganhar badges!*");
} else {
    dv.list(badges);
}

// --- FLASHCARDS ---
dv.paragraph("## 🔄 Flashcards");
const cards = (flashcardsPage && flashcardsPage.flashcards) || [];
const unknown = cards.filter(c => c.status === "unknown").length;
const learning = cards.filter(c => c.status === "learning").length;
const mastered = cards.filter(c => c.status === "mastered").length;
dv.paragraph(`Total: ${cards.length} | ❓ ${unknown} | 📖 ${learning} | ✅ ${mastered}`);

// --- NEXT ACTION ---
dv.paragraph("## 🎯 Próxima Ação");
const nextPhase = p.current_phase;
dv.paragraph(`Continue na **[Fase ${nextPhase}: ${fases[nextPhase]}](./notes/fase-${nextPhase}-fundamentos/01-introducao-setup.md)**`);

}
```
