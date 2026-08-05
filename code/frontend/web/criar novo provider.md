
**1. Criar o provider**

Escolhe **Application** e **Rsbuild**.

```bash
pnpm create module-federation@latest
```

---

**2. Criar o `module-federation.config.ts`**

```typescript
import { createModuleFederationConfig } from '@module-federation/rsbuild-plugin';

export default createModuleFederationConfig({
  name: 'my_provider',          // nome único, sem hífen
  exposes: {
    './ProviderComponent': './src/components/ProviderComponent.tsx',
  },
  shared: {
    react: { singleton: true },
    'react-dom': { singleton: true },
  },
});
```

---

**4. Configurar o `rsbuild.config.ts`**

```typescript
import { defineConfig } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';
import { pluginModuleFederation } from '@module-federation/rsbuild-plugin';
import moduleFederationConfig from './module-federation.config';

export default defineConfig({
  plugins: [pluginReact(), pluginModuleFederation(moduleFederationConfig)],
  server: { port: 3002 },   // porta diferente dos outros providers
});
```

---

**5. Registrar no consumer**

No `rsbuild.config.ts` do consumer, adiciona o novo remote:

typescript

```typescript
remotes: {
  highlight_card: 'highlight_card@http://localhost:3001/mf-manifest.json',
  my_provider: 'my_provider@http://localhost:3002/mf-manifest.json',  // novo
},
```

---

**6. Usar no consumer**

```typescript
import ProviderComponent from 'my_provider/ProviderComponent';

export default function App() {
  return (
    <div>
      <ProviderComponent />
    </div>
  );
}
```

---

Resumindo: cada provider novo é uma porta diferente + um `name` único. O consumer só precisa saber a URL do `mf-manifest.json` de cada um.