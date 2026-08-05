
    export type RemoteKeys = 'highlight_card/ProviderComponent';
    type PackageType<T> = T extends 'highlight_card/ProviderComponent' ? typeof import('highlight_card/ProviderComponent') :any;