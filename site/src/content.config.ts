import { defineCollection } from 'astro:content';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';
import { z } from 'astro/zod';
import { raporVerisi } from './yerel';

// Rapor metinleri sitenin kendi Markdown işleyicisiyle HTML'e çevrilir; sadece yerel derlemede dolar (src/yerel.ts).
const raporlar = defineCollection({
	loader: {
		name: 'ship-raporlar',
		load: async ({ store, renderMarkdown }) => {
			store.clear();
			for (const g of raporVerisi()) {
				for (const r of g.raporlar) {
					store.set({ id: r.yol, data: {}, body: r.metin, rendered: await renderMarkdown(r.metin) });
				}
			}
		},
	},
});

export const collections = {
	docs: defineCollection({ loader: docsLoader(), schema: docsSchema({ extend: z.object({ araclar: z.array(z.string()).optional() }) }) }),
	// Starlight'ın Türkçe çevirisinde olmayan metinler (src/content/i18n/tr.json).
	i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
	raporlar,
};
