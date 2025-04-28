#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Aatrox/CAC/Aatrox_Base" = ContextualActionData {
        mCooldown: f32 = 15
        mSituations: map[hash,embed] = {
            "MoveOrder2D" = ContextualSituation {
                mCoolDownTime: f32 = 20
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Long (from base)"
                        mConditions: list[pointer] = {
                            ContextualConditionMapRegionName {
                                mRegionType: u8 = 4
                                mRegionName: string = "AREA_Base"
                            }
                            ContextualConditionMoveDistance {
                                mDistance: f32 = 2000
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move2DLong"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Near battle R ready"
                        mConditions: list[pointer] = {
                            ContextualConditionMoveDistance {
                                mDistance: f32 = 400
                                mCompareOp: u8 = 3
                            }
                            ContextualConditionRuleCooldown {
                                mRuleCooldown: f32 = 120
                            }
                            ContextualConditionSpell {
                                mSpellSlot: u32 = 3
                                mChildConditions: list[pointer] = {
                                    ContextualConditionSpellIsReady {
                                        mSpellIsReady: bool = true
                                    }
                                }
                            }
                            ContextualConditionNearbyChampionCount {
                                mCount: u32 = 1
                                mCompareOp: u8 = 3
                            }
                            ContextualConditionNearbyChampionCount {
                                mTeamCompareOp: u8 = 1
                                mCount: u32 = 2
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move3DRReady"
                            mAllyEventName: string = "Move3DRReady"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Standard"
                        mConditions: list[pointer] = {
                            ContextualConditionMoveDistance {
                                mDistance: f32 = 400
                                mCompareOp: u8 = 3
                            }
                            ContextualConditionMoveDistance {
                                mDistance: f32 = 2000
                                mCompareOp: u8 = 5
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move2DStandard"
                        }
                    }
                }
            }
            "FirstMove2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Pantheon"
                        mConditions: list[pointer] = {
                            ContextualConditionAnyOtherHero {
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Pantheon/CharacterRecords/Root"
                                        }
                                    }
                                    ContextualConditionIsAlly {}
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move2DFirstPantheon"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "First Move"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move2DLong"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "AttackChampion2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Pantheon"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Pantheon/CharacterRecords/Root"
                                        }
                                    }
                                    ContextualConditionCharacterDistance {
                                        mDistance: f32 = 700
                                    }
                                }
                            }
                            ContextualConditionRuleCooldown {
                                mRuleCooldown: f32 = 30
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 2
                            mSelfEventName: string = "Attack2DPantheon"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Tryndamere"
                        mConditions: list[pointer] = {
                            ContextualConditionRuleCooldown {
                                mRuleCooldown: f32 = 30
                            }
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Tryndamere/CharacterRecords/Root"
                                        }
                                    }
                                    ContextualConditionCharacterDistance {
                                        mDistance: f32 = 700
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 2
                            mSelfEventName: string = "Attack2DTryndamere"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Zoe"
                        mConditions: list[pointer] = {
                            ContextualConditionRuleCooldown {
                                mRuleCooldown: f32 = 30
                            }
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Zoe/CharacterRecords/Root"
                                        }
                                    }
                                    ContextualConditionCharacterDistance {
                                        mDistance: f32 = 700
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 2
                            mSelfEventName: string = "Attack2DZoe"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "KillChampion" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Aatrox"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Aatrox/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DAatrox"
                            mEnemyEventName: string = "Kill3DAatrox"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Anivia"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Anivia/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DAnivia"
                            mEnemyEventName: string = "Kill3DAnivia"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Camille"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Camille/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DCamille"
                            mEnemyEventName: string = "Kill3DCamille"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Darius"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Darius/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DDarius"
                            mEnemyEventName: string = "Kill3DDarius"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Fiora"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Fiora/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DFiora"
                            mEnemyEventName: string = "Kill3DFiora"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Gangplank"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Gangplank/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DGangplank"
                            mEnemyEventName: string = "Kill3DGangplank"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Garen"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Garen/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DGaren"
                            mEnemyEventName: string = "Kill3DGaren"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Illaoi"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Illaoi/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DIllaoi"
                            mEnemyEventName: string = "Kill3DIllaoi"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kaisa"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kaisa/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DKaisa"
                            mEnemyEventName: string = "Kill3DKaisa"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kayle"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kayle/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DKayle"
                            mEnemyEventName: string = "Kill3DKayle"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kayn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kayn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DKayn"
                            mEnemyEventName: string = "Kill3DKayn"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kled"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kled/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DKled"
                            mEnemyEventName: string = "Kill3DKled"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Malphite"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Malphite/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DMalphite"
                            mEnemyEventName: string = "Kill3DMalphite"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Maokai"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Maokai/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DMaokai"
                            mEnemyEventName: string = "Kill3DMaokai"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Morgana"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Morgana/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DMorgana"
                            mEnemyEventName: string = "Kill3DMorgana"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nasus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nasus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DNasus"
                            mEnemyEventName: string = "Kill3DNasus"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nautilus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nautilus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DNautilus"
                            mEnemyEventName: string = "Kill3DNautilus"
                            mWaitForAnnouncerQueue: bool = true
                            mWaitTimeout: f32 = 5
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Ornn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Ornn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DOrnn"
                            mEnemyEventName: string = "Kill3DOrnn"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Pantheon"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Pantheon/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DPantheon"
                            mEnemyEventName: string = "Kill3DPantheon"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Riven"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Riven/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DRiven"
                            mEnemyEventName: string = "Kill3DRiven"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Shen"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Shen/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DShen"
                            mEnemyEventName: string = "Kill3DShen"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Sion"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Sion/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DSion"
                            mEnemyEventName: string = "Kill3DSion"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Taric"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Taric/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DTaric"
                            mEnemyEventName: string = "Kill3DTaric"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Teemo"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Teemo/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DTeemo"
                            mEnemyEventName: string = "Kill3DTeemo"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Tryndamere"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Tryndamere/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DTryndamere"
                            mEnemyEventName: string = "Kill3DTryndamere"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Varus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Varus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 2
                            mSelfEventName: string = "Kill3DVarus"
                            mEnemyEventName: string = "Kill3DVarus"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Zoe"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 6
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Zoe/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Kill3DZoe"
                            mEnemyEventName: string = "Kill3DZoe"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Kill3DGeneral"
                            mEnemyEventName: string = "Kill3DGeneral"
                            mWaitForAnnouncerQueue: bool = true
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "EnemyFirstEncounter" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Taric"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Taric/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DTaric"
                            mEnemyEventName: string = "FirstEncounter3DTaric"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Akali"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Akali/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DAkali"
                            mEnemyEventName: string = "FirstEncounter3DAkali"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Anivia"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Anivia/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DAnivia"
                            mEnemyEventName: string = "FirstEncounter3DAnivia"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Camille"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Camille/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DCamille"
                            mEnemyEventName: string = "FirstEncounter3DCamille"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Darius"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Darius/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DDarius"
                            mEnemyEventName: string = "FirstEncounter3DDarius"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Fiora"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Fiora/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DFiora"
                            mEnemyEventName: string = "FirstEncounter3DFiora"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Galio"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Galio/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DGalio"
                            mEnemyEventName: string = "FirstEncounter3DGalio"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Gangplank"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Gangplank/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DGangplank"
                            mEnemyEventName: string = "FirstEncounter3DGangplank"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Garen"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Garen/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DGaren"
                            mEnemyEventName: string = "FirstEncounter3DGaren"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Illaoi"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Illaoi/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DIllaoi"
                            mEnemyEventName: string = "FirstEncounter3DIllaoi"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Jax"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Jax/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DJax"
                            mEnemyEventName: string = "FirstEncounter3DJax"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kaisa"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kaisa/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKaisa"
                            mEnemyEventName: string = "FirstEncounter3DKaisa"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kayle"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kayle/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKayle"
                            mEnemyEventName: string = "FirstEncounter3DKayle"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kayn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kayn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKayn"
                            mEnemyEventName: string = "FirstEncounter3DKayn"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kennen"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kennen/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKennen"
                            mEnemyEventName: string = "FirstEncounter3DKennen"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Kled"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Kled/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKled"
                            mEnemyEventName: string = "FirstEncounter3DKled"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Malphite"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Malphite/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DMalphite"
                            mEnemyEventName: string = "FirstEncounter3DMalphite"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Maokai"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Maokai/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DMaokai"
                            mEnemyEventName: string = "FirstEncounter3DMaokai"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Morgana"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Morgana/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DMorgana"
                            mEnemyEventName: string = "FirstEncounter3DMorgana"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Mundo"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/DrMundo/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DMundo"
                            mEnemyEventName: string = "FirstEncounter3DMundo"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nasus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nasus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DNasus"
                            mEnemyEventName: string = "FirstEncounter3DNasus"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nautilus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nautilus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DNautilus"
                            mEnemyEventName: string = "FirstEncounter3DNautilus"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Ornn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Ornn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DOrnn"
                            mEnemyEventName: string = "FirstEncounter3DOrnn"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Pantheon"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Pantheon/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DPantheon"
                            mEnemyEventName: string = "FirstEncounter3DPantheon"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Quinn"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Quinn/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DQuinn"
                            mEnemyEventName: string = "FirstEncounter3DQuinn"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Renekton"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Renekton/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DRenekton"
                            mEnemyEventName: string = "FirstEncounter3DRenekton"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Riven"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Riven/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DRiven"
                            mEnemyEventName: string = "FirstEncounter3DRiven"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Rumble"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Rumble/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DRumble"
                            mEnemyEventName: string = "FirstEncounter3DRumble"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Shen"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Shen/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DShen"
                            mEnemyEventName: string = "FirstEncounter3DShen"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Sion"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Sion/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DSion"
                            mEnemyEventName: string = "FirstEncounter3DSion"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Teemo"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Teemo/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DTeemo"
                            mEnemyEventName: string = "FirstEncounter3DTeemo"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Trundle"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Trundle/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DTrundle"
                            mEnemyEventName: string = "FirstEncounter3DTrundle"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Tryndamere"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Tryndamere/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DTryndamere"
                            mEnemyEventName: string = "FirstEncounter3DTryndamere"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Varus"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Varus/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DVarus"
                            mEnemyEventName: string = "FirstEncounter3DVarus"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Yorick"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Yorick/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DYorick"
                            mEnemyEventName: string = "FirstEncounter3DYorick"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Zoe"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Zoe/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DZoe"
                            mEnemyEventName: string = "FirstEncounter3DZoe"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Targon"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterMetadata {
                                        mCategory: string = "faction"
                                        mData: string = "mttargon"
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DTargon"
                            mEnemyEventName: string = "FirstEncounter3DTargon"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Void"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterMetadata {
                                        mCategory: string = "faction"
                                        mData: string = "void"
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DVoid"
                            mEnemyEventName: string = "FirstEncounter3DVoid"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DGeneral"
                            mEnemyEventName: string = "FirstEncounter3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "taunt" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Taunt"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Taunt3DGeneral"
                            mAllyEventName: string = "Taunt3DGeneral"
                            mEnemyEventName: string = "Taunt3DGeneral"
                            mSpectatorEventName: string = "Taunt3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "SpellCast" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "W"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Aatrox/Spells/AatroxWAbility/AatroxW"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "E"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Aatrox/Spells/AatroxEAbility/AatroxE"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "R"
                        mConditions: list[pointer] = {
                            ContextualConditionSpell {
                                mSpellSlot: u32 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                }
            }
            "Laugh" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Laugh"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Laugh3DGeneral"
                            mAllyEventName: string = "Laugh3DGeneral"
                            mEnemyEventName: string = "Laugh3DGeneral"
                            mSpectatorEventName: string = "Laugh3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "AttackMinion2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Minion"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "AttackNeutral2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Neutral"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "Joke" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Joke"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Joke3DGeneral"
                            mAllyEventName: string = "Joke3DGeneral"
                            mEnemyEventName: string = "Joke3DGeneral"
                            mSpectatorEventName: string = "Joke3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "MasteryBadgeStartedNearby" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Mastery Response"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "MasteryResponse3DGeneral"
                            mEnemyEventName: string = "MasteryResponse3DGeneral"
                        }
                        mOverrideCacCooldown: bool = true
                    }
                }
            }
        }
        mObjectPath: string = "Characters/Aatrox/CAC/Aatrox_Base"
    }
}
