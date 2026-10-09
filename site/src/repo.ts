import katalog from './data/katalog.json';

export type Repo = (typeof katalog.repolar)[number];
export const kurulum = {
	proje: { etiket: 'Projeye eklenir', baslik: 'Projeye ekle', aciklama: 'Bu projeye eklenir. Prompt’u kodlama ajanına yapıştır.', tur: 'kurulum' },
	claude: { etiket: "Claude'a kurulur", baslik: "Claude'a kur", aciklama: 'Claude Code’a kurulur. Prompt’u kodlama ajanına yapıştır.', tur: 'claude' },
	codex: { etiket: "Codex'e kurulur", baslik: "Codex'e kur", aciklama: 'Codex’e kurulur. Prompt’u kodlama ajanına yapıştır.', tur: 'codex' },
	uygulama: { etiket: 'Ayrı uygulama', baslik: 'Uygulamayı kur', aciklama: 'Bilgisayarına veya sunucuna ayrı bir program olarak kurulur. Prompt’u kodlama ajanına yapıştır.', tur: 'uygulama' },
	kaynak: { etiket: 'Kaynak, kurulmaz', baslik: 'Kurulmaz; README okunur', aciklama: '', tur: '' },
} as const;
export type Kurulum = keyof typeof kurulum;
export type KurulumTuru = (typeof kurulum)[Exclude<Kurulum, 'kaynak'>]['tur'];

export const yildiz = (n: number | null) => n == null ? '' : n >= 100000 ? `${Math.floor(n / 1000)}k` : n >= 1000 ? (n / 1000).toFixed(1).replace(/\.0$/, '').replace('.', ',') + 'k' : String(n);
export const tarih = (d: string | null) => d ? d.split('-').reverse().join('.') : '';
export const repoAdres = (r: Repo | string) => `/repolar/${(typeof r === 'string' ? r : r.repo).toLowerCase()}/`;
export const kategoriAdi = (ad: string) => ad.replace(/^[^\p{L}\p{N}]+/u, '');
export const eski = (r: Repo) => !!r.son_guncelleme && r.son_guncelleme < new Date(Date.now() - 365 * 864e5).toISOString().slice(0, 10);
export const dikkat = (r: Repo) => r.arsiv || eski(r);
export const prompt = {
	proje: (u: string) => `Şu aracı bu projede kullanmak istiyorum: ${u}\nREADME'sini oku; bu projenin diline ve altyapısına uygun mu söyle. Uygunsa projeye ekle ve nasıl kullanılacağını kısaca göster.`,
	claude: (u: string) => `Şu aracı Claude Code'a kurmak istiyorum: ${u}\nREADME'sini oku ve neyin kurulacağını söyle (skill, eklenti, MCP sunucusu, hook); birden fazla kurulum yolu varsa farklarını anlat. Tüm projelerde mi (kullanıcı düzeyi, ~/.claude) yoksa sadece bu projede mi kurulması gerektiğini öner ve bana sor. Projeye dosya yazacak ya da mevcut ayarları veya CLAUDE.md'yi değiştirecekse önceden söyle. Onaylarsam kur ve nasıl kullanılacağını kısaca göster.`,
	codex: (u: string) => `Şu aracı Codex'e kurmak istiyorum: ${u}\nREADME'sini oku ve Codex için neyin kurulacağını söyle (skill, eklenti, MCP sunucusu, hook); birden fazla kurulum yolu varsa farklarını anlat. Tüm projelerde mi (kullanıcı düzeyi, ~/.codex ya da ~/.agents/skills) yoksa sadece bu projede mi kurulması gerektiğini öner ve bana sor. Projeye dosya yazacak ya da ~/.codex/config.toml'u veya AGENTS.md'yi değiştirecekse önceden söyle. Onaylarsam kur ve nasıl kullanılacağını kısaca göster.`,
	uygulama: (u: string) => `Şu uygulamayı kurmak istiyorum: ${u}\nREADME'sini oku; bu bilgisayara mı (masaüstü uygulaması ya da komut satırı aracı) yoksa bir sunucuya mı (Docker ile çalışan servis) kurulduğunu söyle. İşletim sistemimde çalışıp çalışmadığını ve gereksinimlerini (ekran kartı, Docker, API anahtarı, disk alanı) kontrol et. Kurulum adımlarını göster; onaylarsam kur ve nasıl kullanılacağını kısaca göster.`,
} as const;
export const platform = (u: string) => ({ 'instagram.com': 'Instagram', 'youtube.com': 'YouTube', 'youtu.be': 'YouTube' } as Record<string, string>)[new URL(u).hostname.replace(/^www\./, '')] ?? new URL(u).hostname.replace(/^www\./, '');
