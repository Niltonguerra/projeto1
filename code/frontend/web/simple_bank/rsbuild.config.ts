import { defineConfig } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';
import { pluginModuleFederation } from '@module-federation/rsbuild-plugin';

export default defineConfig({
  plugins: [
    pluginReact(),
    pluginModuleFederation({
      name: 'consumer',
      remotes: {
        // highlight_card: 'highlight_card@http://localhost:3001/mf-manifest.json',
        teste123: 'teste123@http://localhost:3002/mf-manifest.json',  // novo
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
  ],
  server: { port: 3000 },
});