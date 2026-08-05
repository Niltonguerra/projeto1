
    export type RemoteKeys = 'teste123/ProviderComponent';
    type PackageType<T> = T extends 'teste123/ProviderComponent' ? typeof import('teste123/ProviderComponent') :any;