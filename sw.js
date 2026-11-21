const CACHE_NAME = "etec-ds-henrique-v6";
const CORE_ASSETS = [
  "./",
  "./index.html",
  "./COMECE_AQUI.html",
  "./dados_plataforma.js",
  "./manifest.json",
  "./icon.svg",
  "./img/t26_p4_i1.png",
  "./img/t26_p5_i1.jpg",
  "./img/t26_p6_i1.png",
  "./img/t26_p6_i2.png",
  "./img/t26_p7_i1.png",
  "./img/t25_p8_i1.jpg",
  "./img/r21_q4.jpg", "./img/r21_q6a.jpg", "./img/r21_q6b.jpg", "./img/r21_q7.jpg", "./img/r21_q15.png", "./img/r21_q19.png", "./img/r21_q20.png",
  "./img/r22_q21.png", "./img/inf25_tirinha.png", "./img/inf25_grafico.png", "./img/ipi24_triangulos.png", "./img/ipi25_marte.jpg"
];

self.addEventListener("install", (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CORE_ASSETS)).catch(() => {})
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  // Network-First: busca sempre a versão mais recente online, e cai para cache offline se sem sinal
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy)).catch(() => {});
        }
        return res;
      })
      .catch(() => caches.match(event.request))
  );
});
