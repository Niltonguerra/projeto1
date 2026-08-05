
    export type RemoteKeys = 'my_provider/ProviderComponent';
    type PackageType<T> = T extends 'my_provider/ProviderComponent' ? typeof import('my_provider/ProviderComponent') :any;