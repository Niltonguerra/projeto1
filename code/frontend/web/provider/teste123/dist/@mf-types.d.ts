
    export type RemoteKeys = 'REMOTE_ALIAS_IDENTIFIER/ProviderComponent';
    type PackageType<T> = T extends 'REMOTE_ALIAS_IDENTIFIER/ProviderComponent' ? typeof import('REMOTE_ALIAS_IDENTIFIER/ProviderComponent') :any;